from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .models import item
from django.views.generic import View
import random
# Create your views here.


def landing(request):
    return render(request, 'landing.html')


def fight(request):
    # if request == "POST":
    all_objects = item.objects.all()
    random_item_1 = random.choice(all_objects)
    random_item_2 = random.choice(all_objects)
    ai_attack = random_item_1.attack + random_item_2.attack
    ai_defense = random_item_1.defense + random_item_2.defense
    context = {
        "ai_attack": ai_attack,
        "ai_defense": ai_defense,
        "random_item_1": random_item_1,
        "random_item_2": random_item_2,
    }
    return render(request, 'fight_page.html', context)
    # else:
    #     all_objects = item.objects.all()
    #     random_item_1 = random.choice(all_objects)
    #     random_item_2 = random.choice(all_objects)
    #     ai_attack = random_item_1.attack + random_item_2.attack
    #     ai_defense = random_item_1.defense + random_item_2.defense
    #     context = {
    #         "ai_attack" : ai_attack,
    #         "ai_defense" : ai_defense,
    #         "random_item_1" : random_item_1,
    #         "random_item_2" : random_item_2,
    #     }
    #     return render(request, 'fight_page.html', context)


class inventory(View):
    def get(self, request):
        items = item.objects.all
        template = loader.get_template("inventory.html")
        context = {
            "items": items,
        }
        return HttpResponse(template.render(context, request))
        # return HttpResponse("inventory.html")

    def post(self, request):
        items = item.objects.all
        data = item.objects.all()
        template = loader.get_template("inventory.html")
        context = {
            "items": items,
            "data": data,
        }
        return HttpResponse(template.render(context, request))
        # return HttpResponse("inventory.html")

def move_data(request):
    if request.method == 'POST':
        data_models = request.POST.getlist('dataModels')
        for id in data_models:
            try:
                data_model = item.objects.get(id=id)
                context = {
                    "data_model" : data_model,
                }
            except item.DoesNotExist:
                return HttpResponse('Data model not found', status=404)
        return redirect('fight_page', context)
    else:
        return HttpResponse('Invalid request', status=405)