from django.urls import path
from kinopoisk.views import *

urlpatterns = [
    path('', films_list)
    # path("films_list/", films_list, name="films_list"),
    # path("film_person_list/", film_person_list, name="film_person_list"),
    # path("actor_detail/<int:actor_id/", actor_detail, name="actor_detail"),
    # path("composer_detail/<int:composer_id/", composer_detail, name="composer_detail"),
    # path("director_detail/<int:director_id/", director_detail, name="director_detail"),
    # path("film_detail/", film_detail, name="film_detail"),
    # path("genre_detail/", genre_detail, name="genre_detail"),
    # path("producer_detail/<int:producer_id/", producer_detail, name="producer_detail"),
    # path("screenwriter_detail/<int:screenwriter_id/", screenwriter_detail, name="screenwriter_detail"),
]