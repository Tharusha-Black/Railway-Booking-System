from django.shortcuts import render
from django.views import View
from train_schedule_service.models import TrainSchedule

class SearchTrainsView(View):
    def get(self, request):
        # Get unique destinations and start locations from TrainSchedule
        destinations = TrainSchedule.objects.values_list('destination', flat=True).distinct()
        start_locations = TrainSchedule.objects.values_list('start_location', flat=True).distinct()

        # Get unique dates from TrainSchedule
        dates = TrainSchedule.objects.values_list('schedule_date', flat=True).distinct()

        # Retrieve all schedules
        schedules = TrainSchedule.objects.all()

        # Get sorting criteria from request parameters
        sort_date = request.GET.get('sort_date')
        sort_destination = request.GET.get('sort_destination')
        sort_start_location = request.GET.get('sort_start_location')

        # Apply filtering based on selected options
        filters = {}
        if sort_date:
            filters['schedule_date'] = sort_date
        if sort_destination:
            filters['destination'] = sort_destination
        if sort_start_location:
            filters['start_location'] = sort_start_location

        # Filter schedules based on selected criteria
        if filters:
            schedules = schedules.filter(**filters)

        # Render the template with filtered and sorted schedules and other context data
        return render(request, 'train_search_service/schedule_table.html', {
            'schedules': schedules,
            'dates': dates,
            'destinations': destinations,
            'start_locations': start_locations,
            'sort_date': sort_date,
            'sort_destination': sort_destination,
            'sort_start_location': sort_start_location,
        })
