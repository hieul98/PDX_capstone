from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import attack_item, defense_item, player
# Create your views here.

def landing(request):
    return render(request, 'landing.html')

def inventory(request):
    players = player.objects.all()
    attack_items = attack_item.objects.all()
    defense_items = defense_item.objects.all()
    template = loader.get_template("inventory.html")
    context = {
        "attack_items" : attack_items, 
        "defense_items" : defense_items,
        "players" : players}
    return HttpResponse(template.render(context, request))




