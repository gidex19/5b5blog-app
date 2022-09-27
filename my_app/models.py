from pyexpat import model
from time import time
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50, default='My title')
    body = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post Object: {self.title} by {self.owner}"

    def get_absolute_url(self):
        return reverse('detailpage', kwargs={'pk': self.id})
