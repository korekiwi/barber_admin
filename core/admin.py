from django.contrib import admin
from core.models import Master, Service, Visit


class VisitInline(admin.TabularInline):
    model = Visit
    extra = 0
    readonly_fields = ("created_at",)
    fields = ("name", "phone", "status", "created_at")
    max_num = 10
    ordering = ("-created_at",)


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone")
    inlines = [VisitInline]
    filter_horizontal = ("services",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")
    search_fields = ("name", "description")
    list_display_links = ("name", "price")


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "comment", "status",)
    list_display_links = ("name",)
    list_editable = ("status",)