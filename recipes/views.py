from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.db.models import Q
from recipes.models import Category, Recipe
from utils.pagination import make_pagination

PER_PAGE = 9

def home(request):
    categories = Category.objects.order_by('name')
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    context={
        'categories': categories,
        'recipes': page_obj,
        'pagination_range': pagination_range
    }

    return render(request, 'recipes/home.html', context)

def category(request, slug):
    category = Category.objects.get(slug=slug)
    recipes = Recipe.objects.filter(
        category=category,
        is_published=True,
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    context={
        'recipes':  page_obj,
        'pagination_range': pagination_range,
        'category': category,
    }

    return render(request, 'recipes/category.html', context)

def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)
    category = recipe.category

    context={
        'recipe': recipe,
        'category': category,
    }
    return render(request, 'recipes/single-recipe.html', context)


def search(request):
    search_term = request.GET.get('q', '').strip()

    if search_term == '':
            return redirect('recipes:home')
    
     # Verificar se o termo de pesquisa corresponde a uma categoria
    category = Category.objects.filter(name__icontains=search_term).first()

    if category:
        # Se corresponder a uma categoria, filtrar as receitas associadas a essa categoria
        recipes = Recipe.objects.filter(category=category, is_published=True).order_by('-id')
        categories = [category]  # Passar a categoria encontrada para o template
    else:
        # Se não corresponder a uma categoria, pesquisar nas receitas
        recipes = Recipe.objects.filter(
            Q(title__icontains=search_term) | Q(description__icontains=search_term),
            is_published=True
        ).order_by('-id')
        categories = []  # Não há categorias para passar para o template

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    context = {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'categories': categories,
    }

    return render(request, 'recipes/search.html', context)