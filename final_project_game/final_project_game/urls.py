"""final_project_game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_game_app import views
from main_game_app.views import inventory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing, name='landing'),
    path('inventory/', inventory.as_view(), name='inventory_page'),
    path('fight/', views.fight, name='fight_page'),
    path('move-data/', views.move_data, name="move_data")
]
