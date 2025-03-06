from django.contrib import admin
from core.models import Master, Service, Visit

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")
    search_fields = ("name", "description")
    list_display_links = ("name", "price")

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "comment", "status",)
    list_display_links = ("name",)