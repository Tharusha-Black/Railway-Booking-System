from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.views import View
from .forms import TrainForm, TrainScheduleForm
from .models import Train, TrainSchedule
from django.utils.decorators import method_decorator


class DashboardView(View):
    def get(self, request):
        trains = Train.objects.all()
        schedules = TrainSchedule.objects.all()
        return render(request, 'train_schedule_service/dashboard.html', {'trains': trains, 'schedules': schedules})

class EditTrainView(View):
    def get(self, request, train_id):
        train = get_object_or_404(Train, pk=train_id)
        form = TrainForm(instance=train)
        return render(request, 'train_schedule_service/train_add_form.html', {'form': form})

    def post(self, request, train_id):
        train = get_object_or_404(Train, pk=train_id)
        form = TrainForm(request.POST, instance=train)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        return render(request, 'train_schedule_service/train_add_form.html', {'form': form})

class DeleteTrainView(View):
    def post(self, request, train_id):
        train = get_object_or_404(Train, pk=train_id)
        train.delete()
        return redirect('dashboard')

class AddTrainView(View):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def get(self, request):
        form = TrainForm()
        return render(request, 'train_schedule_service/train_add_form.html', {'form': form})

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def post(self, request):
        form = TrainForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Train successfully added!')
            return redirect('dashboard')
        return render(request, 'train_schedule_service/train_add_form.html', {'form': form})

class ScheduleTrainView(View):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def get(self, request):
        form = TrainScheduleForm()
        return render(request, 'train_schedule_service/schedule_form.html', {'form': form})

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def post(self, request):
        form = TrainScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        return render(request, 'train_schedule_service/schedule_form.html', {'form': form})

class EditScheduleView(View):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def get(self, request, schedule_id):
        schedule = get_object_or_404(TrainSchedule, pk=schedule_id)
        form = TrainScheduleForm(instance=schedule)
        return render(request, 'train_schedule_service/schedule_form.html', {'form': form})

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def post(self, request, schedule_id):
        schedule = get_object_or_404(TrainSchedule, pk=schedule_id)
        form = TrainScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            messages.success(request, 'Schedule successfully updated!')
            return redirect('dashboard')
        return render(request, 'train_schedule_service/schedule_form.html', {'form': form})

class DeleteScheduleView(View):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def post(self, request, schedule_id):
        schedule = get_object_or_404(TrainSchedule, pk=schedule_id)
        schedule.delete()
        messages.success(request, 'Schedule successfully deleted!')
        return redirect('dashboard')
