from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Note(models.Model):
    text = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_date(self):
        return timezone.now() - datetime.timedelta(days=1)
