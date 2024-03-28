from django.contrib import admin
from films.models import *
# Register your models here.
@admin.register(FilmPerson)
class FilmPersonAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "role",
        "name",
    )

@admin.register(Genre)
class Genreadmin(admin.ModelAdmin):
    list_display=(
        "id",
        "name",
    )

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "title",
        "genres",
        "duration",
    )

@admin.register(FilmReview)
class FilmReviewAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "author",
        "film",
    )