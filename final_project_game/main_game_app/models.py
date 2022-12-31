from django.db import models

# Create your models here.
class attack_item(models.Model):
    name = models.CharField(max_length=500)
    attack = models.IntegerField()
    def __str__(self):
        return self.name

class defense_item(models.Model):
    name = models.CharField(max_length=500)
    defense = models.IntegerField()
    def __str__(self):
        return self.name

class player(models.Model):
    name = models.CharField(max_length=30)
    attack_items = models.ManyToManyField(attack_item, related_name='players')
    defense_items = models.ManyToManyField(defense_item, related_name='players')
    def __str__(self):
        return self.name
