from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    fav_films = models.ManyToManyField("kinopoisk.Movie")
    