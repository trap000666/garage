# garage/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.utils import timezone
from .models import Booking, STATUS_CHOICES
from .forms import BookingForm, BookingStatusForm
import datetime


def home(request):
    return render(request, 'garage/home.html')


def book_service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_success', pk=booking.pk)
    else:
        form = BookingForm()
    return render(request, 'garage/book.html', {'form': form})


def booking_success(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'garage/booking_success.html', {'booking': booking})


def staff_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'garage/login.html', {'form': form})


def staff_logout(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard(request):
    # Filters
    status_filter = request.GET.get('status', '')
    date_filter = request.GET.get('date', '')

    bookings = Booking.objects.all()

    if status_filter:
        bookings = bookings.filter(status=status_filter)
    if date_filter:
        bookings = bookings.filter(preferred_date=date_filter)

    # Summary counts
    today = datetime.date.today()
    context = {
        'bookings': bookings,
        'status_filter': status_filter,
        'date_filter': date_filter,
        'status_choices': STATUS_CHOICES,
        'total': Booking.objects.count(),
        'pending': Booking.objects.filter(status='pending').count(),
        'in_progress': Booking.objects.filter(status='in_progress').count(),
        'completed': Booking.objects.filter(status='completed').count(),
        'today_jobs': Booking.objects.filter(preferred_date=today).count(),
    }
    return render(request, 'garage/dashboard.html', context)


@login_required
def job_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingStatusForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully!')
            return redirect('dashboard')
    else:
        form = BookingStatusForm(instance=booking)
    return render(request, 'garage/job_detail.html', {'booking': booking, 'form': form})


@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking deleted.')
        return redirect('dashboard')
    return render(request, 'garage/confirm_delete.html', {'booking': booking})