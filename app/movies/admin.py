from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Movie


# @admin.register(CustomUser)
# class UserAdmin(DefaultUserAdmin):
#     pass


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
