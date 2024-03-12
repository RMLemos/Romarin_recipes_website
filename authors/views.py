from django.shortcuts import redirect, render
from django.http import Http404
from authors.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from recipes.models import Recipe
from authors.forms import AuthorRecipeForm
from django.utils.text import slugify


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('recipes:home')


    return render(
        request,
        'authors/register.html',
        {
            'form': form
        }
    )


def login_view(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            authenticated_user = authenticate(
                username=form.cleaned_data.get('username', ''),
                password=form.cleaned_data.get('password', ''),
            )

            if authenticated_user is not None:
                login(request, authenticated_user)
            else:
                messages.error(request, 'Invalid credentials')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'authors/login.html', {
        'form': form,
    })


@login_required(login_url='authors:login')
def dashboard(request):
    recipes = Recipe.objects.filter(
        is_published=False,
        author=request.user
    )

    context={
            'recipes': recipes,
        }

    return render(request, 'authors/dashboard.html', context)


@login_required(login_url='authors:login')
def dashboard_recipe_new(request):
    form = AuthorRecipeForm(
        data=request.POST or None,
        files=request.FILES or None,
    )

    if form.is_valid():
        recipe: Recipe = form.save(commit=False)

        recipe.author = request.user
        recipe.is_published = False
        recipe.slug = slugify(recipe.title)

        recipe.save()

        return redirect(
            reverse('authors:dashboard')
        )
    
    context={
            'form': form,
            'form_action': reverse('authors:dashboard_recipe_new')
        }

    return render(request, 'authors/dashboard_recipe.html', context)


@login_required(login_url='authors:login')
def dashboard_recipe_edit(request, id):
    recipe = Recipe.objects.filter(
        is_published=False,
        author=request.user,
        pk=id,
    ).first()

    if not recipe:
        raise Http404()
    
    form = AuthorRecipeForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=recipe
    )
    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.is_published = False
        recipe.slug = slugify(recipe.title)
        recipe.save()
        return redirect(reverse('authors:dashboard')
                        )
    return render(
        request,
        'authors/dashboard_recipe_update.html',
        context={
            'form': form,
            'recipe_id': id
        }
    )


@login_required(login_url='authors:login')
def dashboard_recipe_delete(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    print(POST)
    id = POST.get('id')
    print(f' este é o {id}')
    recipe = Recipe.objects.filter(
        is_published=False,
        author=request.user,
        pk=id,
    ).first()
    print(f' esta é a {recipe}')
    if not recipe:
        raise Http404()
    recipe.delete()
    return redirect('authors:dashboard')