from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Map(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  # Clé étrangère avec une valeur par défaut de None
    lat = models.FloatField()
    lon = models.FloatField()
    date = models.DateTimeField()
    photo = models.ImageField(upload_to="photos/")

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        return ''