# garage/models.py

from django.db import models

SERVICE_CHOICES = [
    ('oil_change', 'Oil Change'),
    ('tyre_change', 'Tyre Change'),
    ('brake_service', 'Brake Service'),
    ('engine_repair', 'Engine Repair'),
    ('electrical', 'Electrical Repair'),
    ('body_work', 'Body Work'),
    ('full_service', 'Full Service'),
    ('diagnostics', 'Vehicle Diagnostics'),
    ('other', 'Other'),
]

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
]


class Booking(models.Model):
    # Customer Info
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField()

    # Vehicle Info
    vehicle_make = models.CharField(max_length=50)   # e.g. Toyota
    vehicle_model = models.CharField(max_length=50)  # e.g. Corolla
    vehicle_year = models.CharField(max_length=4)
    number_plate = models.CharField(max_length=20)

    # Service Info
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    description = models.TextField(blank=True, help_text="Any extra details about the problem")
    preferred_date = models.DateField()
    preferred_time = models.TimeField()

    # Status & Tracking
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    mechanic_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.vehicle_make} {self.vehicle_model} ({self.preferred_date})"

    class Meta:
        ordering = ['preferred_date', 'preferred_time']