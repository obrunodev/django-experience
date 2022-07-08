from django.db import models


class Genre(models.TextChoices):
    TERROR = 'Terror'
    DRAMA = 'Drama'
    ROMANCE = 'Romance'