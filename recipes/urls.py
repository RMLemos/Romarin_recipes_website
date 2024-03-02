from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="single-recipe"),
]