from django.shortcuts import render
from .models import *

# Create your views here.
def films_list(request):
    return render(request,"films/films_list.html")
# def actor_detail(request, actor_id):
#     actor = FilmPerson.objects.filter(role=FilmPerson.RoleType.ACTOR)
#     return render(request,"films/actor_detail.html")
# def composer_detail(request, composer_id):
#     composer = FilmPerson.objects.filter(role=FilmPerson.RoleType.COMPOSER)
#     return render(request,"films/composer_detail.html")
# def director_detail(request, director_id):
#     director = FilmPerson.objects.filter(role=FilmPerson.RoleType.DIRECTOR)
#     return render(request,"films/director_detail.html")
# def film_detail(request):
#     return render(request,"films/def film_detail.html")
# def genre_detail(request):
#     return render(request,"films/genre_detail.html")
# def producer_detail(request, producer_id):
#     producer = FilmPerson.objects.filter(role=FilmPerson.RoleType.PRODUCER)
#     return render(request,"films/def producer_detail.html")
# def screenwriter_detail(request, screenwriter_id):
#     screenwriter = FilmPerson.objects.filter(role=FilmPerson.RoleType.SCREENWRITER)
#     return render(request,"films/def screenwriter_detail.html")
# def film_person_list(request):
#     return render(request,"films/def film_person_list.html")

