from django.db import models

# Create your models here.
class player(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class item(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name