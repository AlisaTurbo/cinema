from django.urls import path
from films.views import *

urlpatterns = [
    path("films_list/", films_list, name="films_list"),
    path("film_person_list/", film_person_list, name="film_person_list"),
    path("actor_detail/", actor_detail, name="actor_detail"),
    path("composer_detail/", composer_detail, name="composer_detail"),
    path("director_detail/", director_detail, name="director_detail"),
    path("film_detail/", film_detail, name="film_detail"),
    path("genre_detail/", genre_detail, name="genre_detail"),
    path("producer_detail/", producer_detail, name="producer_detail"),
    path("screenwriter_detail/", screenwriter_detail, name="screenwriter_detail"),
]