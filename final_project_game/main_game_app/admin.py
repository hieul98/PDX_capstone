from django.contrib import admin
from .models import attack_item, defense_item, player

# Register your models here.
admin.site.register(attack_item)
admin.site.register(player)
admin.site.register(defense_item)