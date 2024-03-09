from django.shortcuts import redirect, render
from authors.forms import RegisterForm

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