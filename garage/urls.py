# garage/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_service, name='book_service'),
    path('book/success/<int:pk>/', views.booking_success, name='booking_success'),
    path('login/', views.staff_login, name='login'),
    path('logout/', views.staff_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('job/<int:pk>/delete/', views.delete_booking, name='delete_booking'),
]