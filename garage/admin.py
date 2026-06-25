# garage/admin.py

from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'vehicle_make', 'vehicle_model',
                    'number_plate', 'service_type', 'preferred_date', 'status']
    list_filter = ['status', 'service_type', 'preferred_date']
    search_fields = ['customer_name', 'number_plate', 'customer_phone']
    list_editable = ['status']