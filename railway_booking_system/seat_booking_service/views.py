from io import BytesIO
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.db.utils import IntegrityError
from .models import Seat
from train_schedule_service.models import TrainSchedule
from user_management.models import RailwayUser

class SeatBookView(View):
    @method_decorator(login_required)
    def get(self, request, sch_id):
        user_id = request.user.id
        seat_numbers = [str(i) for i in range(1, 11)]
        selected_query = Seat.objects.filter(schedule_id=sch_id).values_list('seat_numbers', flat=True)
        selected_seats = [seat for sublist in selected_query for seat in sublist.split(',')]
        unique_seats_query = Seat.objects.filter(user_id=user_id,schedule_id=sch_id).values_list('seat_numbers', flat=True)
        unique_seats = [seat for sublist in unique_seats_query for seat in sublist.split(',')]
        unique_seats_count = len(unique_seats)
        return render(request, 'seat_booking_service/seats.html', {
            'schedule_id': sch_id,
            'user_id': user_id,
            'seat_numbers': seat_numbers,
            'selected_seats': selected_seats,
            'unique_seats': unique_seats_count
        })

class SeatReservationView(View):
    @method_decorator(login_required)
    def get(self, request):
        user_id = request.GET.get('user_id')
        schedule_id = request.GET.get('schedule_id')
        selected_seats = request.GET.get('selected_seats')

        try:
            user_data = RailwayUser.objects.get(id=user_id)
            schedule_data = TrainSchedule.objects.get(id=schedule_id)
            seat, created = Seat.objects.get_or_create(user=user_data, schedule=schedule_data)
            if not created:
                existing_seat_numbers = seat.seat_numbers
                if existing_seat_numbers:
                    updated_seat_numbers = existing_seat_numbers + "," + selected_seats
                else:
                    updated_seat_numbers = selected_seats
                seat.seat_numbers = updated_seat_numbers
                seat.save()

            pdf = self.render_to_pdf('seat_booking_service/x.html', {'schedule_data': schedule_data, 'user_data': user_data, 'seat_numbers': selected_seats})
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="booking_invoice.pdf"'
                return response
            else:
                return HttpResponse("Failed to generate PDF", status=500)
        except (RailwayUser.DoesNotExist, TrainSchedule.DoesNotExist):
            return JsonResponse({'error': 'User or TrainSchedule does not exist'}, status=400)
        except IntegrityError:
            return JsonResponse({'error': 'Failed to book seats. Please try again later.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def render_to_pdf(self, template_src, context_dict):
        template = get_template(template_src)
        html = template.render(context_dict)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
        if not pdf.err:
            return result.getvalue()
        return None
