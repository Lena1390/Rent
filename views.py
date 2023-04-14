from django.shortcuts import render
from .models import announcement


def index(request):
    return render(request, 'main/index.html')


def basket(request):
    return render(request, 'main/basket.html')


def catalog(request):
    tasks = announcement.objects.all()
    return render(request, 'main/catalog.html', {'title': 'Каталог товаров', 'tasks': tasks})

