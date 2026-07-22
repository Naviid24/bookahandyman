from django.contrib import admin
from .models import Job
# Register your models here.

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "customer_email",
        "customer_phone",
        "status",
        "created_at",
    )

    list_filter = ("status", "created_at")

    search_fields = (
        "customer_name",
        "customer_email",
        "customer_phone",
        "description",
    )
