from django.shortcuts import get_object_or_404, render
from recipes.models import Category, Recipe

def home(request):
    categories = Category.objects.order_by('name')
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/home.html', context={
        'categories': categories,
        'recipes': recipes,
    })

def category(request, slug):
    category = Category.objects.get(slug=slug)
    recipes = Recipe.objects.filter(
        category=category,
        is_published=True,
    ).order_by('-id')
    return render(request, 'recipes/category.html', context={
        'recipes': recipes,
        'category': category,
    })

def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)
    category = recipe.category

    return render(request, 'recipes/single-recipe.html', context={
        'recipe': recipe,
        'category': category,
    })