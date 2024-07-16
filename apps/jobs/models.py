from core.models import BaseModel
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Job(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'))

    class Meta:
        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')
    
    def __str__(self):
        return self.title
