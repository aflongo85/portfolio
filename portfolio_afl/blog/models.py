from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):

    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    body_text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now())
