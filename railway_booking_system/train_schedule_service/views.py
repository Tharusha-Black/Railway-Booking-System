from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import TrainForm, TrainScheduleForm
from django.contrib import messages  # Import messages module
from .models import Train, TrainSchedule
from django.shortcuts import get_object_or_404

def dashboard(request):
    trains = Train.objects.all()
    schedules = TrainSchedule.objects.all()
    return render(request, 'train_schedule_service/dashboard.html', {'trains': trains, 'schedules': schedules})

def edit_train(request, train_id):
    train = get_object_or_404(Train, pk=train_id)
    if request.method == 'POST':
        form = TrainForm(request.POST, instance=train)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TrainForm(instance=train)
    return render(request, 'train_schedule_service/train_add_form.html', {'form': form})

def delete_train(request, train_id):
    train = get_object_or_404(Train, pk=train_id)
    if request.method == 'POST':
        train.delete()
        return redirect('dashboard')
    return render(request, 'train_schedule_service/train_confirm_delete.html', {'train': train})

@user_passes_test(lambda u: u.is_superuser)
def add_train(request):
    if request.method == 'POST':
        form = TrainForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Train successfully added!')
            return redirect('dashboard')  # Redirect to the dashboard with a success message
    else:
        form = TrainForm()
    return render(request, 'train_schedule_service/train_add_form.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def schedule_train(request):
    if request.method == 'POST':
        form = TrainScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to a success page
    else:
        form = TrainScheduleForm()
    return render(request, 'train_schedule_service/schedule_form.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def edit_schedule(request, schedule_id):
    schedule = get_object_or_404(TrainSchedule, pk=schedule_id)
    if request.method == 'POST':
        form = TrainScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            messages.success(request, 'Schedule successfully updated!')
            return redirect('dashboard')
    else:
        form = TrainScheduleForm(instance=schedule)
    return render(request, 'train_schedule_service/schedule_form.html', {'form': form})

# View to delete a train schedule
@user_passes_test(lambda u: u.is_superuser)
def delete_schedule(request, schedule_id):
    schedule = get_object_or_404(TrainSchedule, pk=schedule_id)
    if request.method == 'POST':
        schedule.delete()
        messages.success(request, 'Schedule successfully deleted!')
        return redirect('dashboard')
    return render(request, 'train_schedule_service/schedule_confirm_delete.html', {'schedule': schedule})