from django.db import models

# Create your models here.

class item(models.Model):
    name = models.CharField(max_length=500)
    defense = models.IntegerField()
    attack = models.IntegerField()
    def __str__(self):
        return self.name

