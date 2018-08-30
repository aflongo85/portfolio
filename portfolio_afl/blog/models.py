from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):

    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=60)
    subtitle = models.CharField(max_length=100, default='')
    body_text = models.TextField(default='')
    pub_date = models.DateTimeField(timezone.now())

    def summary(self):
        return self.body[:100]

    def pretty_date(self):
        return self.pub_date.strftime('%e %b %Y')