from django.shortcuts import render

# Create your views here.
def films_list(request):
    return render(request,"films/films_list.html")
def actor_detail(request):
    return render(request,"films/actor_detail.html")
def composer_detail(request):
    return render(request,"films/composer_detail.html")
def director_detail(request):
    return render(request,"films/director_detail.html")
def film_detail(request):
    return render(request,"films/def film_detail.html")
def genre_detail(request):
    return render(request,"films/genre_detail.html")
def producer_detail(request):
    return render(request,"films/def producer_detail.html")
def screenwriter_detail(request):
    return render(request,"films/def screenwriter_detail.html")
def film_person_list(request):
    return render(request,"films/def film_person_list.html")