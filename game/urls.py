from django.urls import path  

from .views import number_game

urlpatterns = [
    path('', number_game, name='number_game'),
]