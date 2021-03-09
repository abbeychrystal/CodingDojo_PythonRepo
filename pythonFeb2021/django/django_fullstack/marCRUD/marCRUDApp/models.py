from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class ChickenManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        if len(reqPOST["chicken_name"])<2:
            errors["name"] = "You must enter a name to continue"
        if len(reqPOST["chicken_color"])<2:
            errors["color"] = "You must enter a color to continue"
        return errors

class Chicken(models.Model):
    name = models.TextField()
    color = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ChickenManager()
