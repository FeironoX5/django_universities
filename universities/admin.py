from django.contrib import admin

from .models import University, Olympiad


@admin.register(Olympiad)
class OlympiadAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "url",)
    list_display_links = ("name",)
    search_fields = ("name",)


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ("short_name", "url",)
    list_display_links = ("short_name",)
    search_fields = ("short_name", "full_name",)
