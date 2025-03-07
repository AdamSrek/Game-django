from django.shortcuts import render

# Create your views here.

def number_game(request):
    return render(request, 'game/index.html')
