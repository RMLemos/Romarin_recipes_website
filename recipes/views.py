from django.shortcuts import render
from recipes.models import Category, Recipe

def home(request):
    categories = Category.objects.order_by('name')
    recipes = Recipe.objects.order_by('-id')
    return render(request, 'recipes/home.html', context={
        'categories': categories,
        'recipes': recipes,
    })


def recipe(request, id):
    return render(request, 'recipes/home.html', context={
        'name': 'Luiz Otávio',
    })