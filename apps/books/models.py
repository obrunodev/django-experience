from apps.books.managers import PublishedManager
from core.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(BaseModel):

    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        PUBLISHED = 'PUBLISHED', 'Published'

    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'), blank=True, null=True)
    status = models.CharField(_('Book status'), max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDING)

    # Managers
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['title']
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
    
    def __str__(self):
        return self.title
