from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    # ninjas = a list of ninjas associated with a given dojo
    def __repr__(self):
        return "Name: {}".format(self.name)

class Ninja(models.Model):
    dojo_id = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    desc = models.TextField(default="none")

    def __repr__(self):
        return "{self.first_name} {self.last_name}".format(self=self)