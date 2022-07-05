from django.db import models


class Seniority(models.TextChoices):
    JUNIOR = 'JR'
    PLENO = 'PL'
    SENIOR = 'SR'
