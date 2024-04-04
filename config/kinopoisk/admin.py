from django.contrib import admin
from kinopoisk.models import *
# Register your models here.
@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "role",
        "name",
    )

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
   list_display=(
        "id",
        "name",
    )

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "title",
        "duration",
    )

@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "author",
        "movie",
    )