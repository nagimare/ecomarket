from django.db import models
from django.db.models import Model
from django.utils import timezone


class Info(Model):
    title = models.CharField(max_length=255, null=False)
    content = models.CharField(max_length=255, null=False)
    post_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='назоваите фото')
