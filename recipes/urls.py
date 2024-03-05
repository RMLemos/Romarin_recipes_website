from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<slug:slug>', views.category, name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]