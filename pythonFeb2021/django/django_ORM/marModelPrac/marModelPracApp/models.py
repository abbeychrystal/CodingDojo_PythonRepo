from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Cow(models.Model):
    name = models.CharField(max_length=45)
    num_blades_grass_eaten = models.IntegerField()
    fav_activity = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)