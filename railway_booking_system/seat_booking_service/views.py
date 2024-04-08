from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Seat
from django.db.utils import IntegrityError
from train_schedule_service.models import TrainSchedule
from user_management.models import RailwayUser
import io
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required


def ticket(request):
    return render(request, 'seat_booking_service/x.html')

@login_required
def seat_book(request,sch_id):
    user_id = request.user.id
    print(user_id)
    seat_numbers = [str(i) for i in range(1, 11)]
    selected_query = Seat.objects.filter(schedule_id=sch_id).values_list('seat_numbers', flat=True)
    unique_seats_query = Seat.objects.filter(user_id=user_id).values_list('seat_numbers', flat=True)
    unique_seats_list = [seat.split(',') for seat in unique_seats_query]
    unique_seats = []
    for item in unique_seats_list:
        for i in item:
            unique_seats.append(i)
    selected_list = [seat.split(',') for seat in selected_query]
    unique_seats_count = len(unique_seats)
    selected_seats = []
    for item in selected_list:
        for i in item:
            selected_seats.append(i)
    return render(request, 'seat_booking_service/seats.html', {'schedule_id': sch_id, 'user_id': user_id, 'seat_numbers': seat_numbers,'selected_seats': selected_seats, 'unique_seats':unique_seats_count})

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def reserved_seats(request):
    user_id = request.GET.get('user_id')
    schedule_id = request.GET.get('schedule_id')
    selected_seats = request.GET.get('selected_seats')

    try:
        # Retrieve the related objects
        user_data = RailwayUser.objects.get(id=user_id)
        schedule_data = TrainSchedule.objects.get(id=schedule_id)

        # Try to get the existing Seat object for the user and schedule
        seat, created = Seat.objects.get_or_create(user=user_data, schedule=schedule_data)

        # If the object already exists, update the selected seats
        if not created:
            existing_seat_numbers = seat.seat_numbers
            updated_seat_numbers = existing_seat_numbers + "," + selected_seats
            seat.seat_numbers = updated_seat_numbers
            seat.save()

        # Generate PDF
        pdf = render_to_pdf('seat_booking_service/x.html', {'schedule_data': schedule_data, 'user_data': user_data, 'seat_numbers': selected_seats})
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="booking_invoice.pdf"'
            return response
        else:
            return HttpResponse("Failed to generate PDF", status=500)
    except RailwayUser.DoesNotExist:
        return JsonResponse({'error': 'RailwayUser with id {} does not exist'.format(user_id)}, status=400)
    except TrainSchedule.DoesNotExist:
        return JsonResponse({'error': 'TrainSchedule with id {} does not exist'.format(schedule_id)}, status=400)
    except IntegrityError:
        return JsonResponse({'error': 'Failed to book seats. Please try again later.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
