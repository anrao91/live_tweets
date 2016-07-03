from __future__ import unicode_literals

from django.utils import timezone as django_timezone
from django.db import models

# Create your models here.

class Tweet(models.Model):
    hashtag = models.CharField(max_length=140, null=False, blank=False)
    text = models.CharField(max_length=140, null=False, blank=False)
    created_at = models.DateTimeField(null=False, default=django_timezone.now)

