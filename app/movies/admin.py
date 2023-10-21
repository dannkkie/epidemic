from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "year",
        "type",
        "poster",
    )
    list_display = (
        "title",
        "year",
        "type",
        "poster",
    )
