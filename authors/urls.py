from django.urls import path
from authors import views

app_name = 'authors'

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login_view, name="login"),
    #path('logout/', views.logout_view, name='logout'),
    

    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/recipe/new/', views.dashboard_recipe_new, name='dashboard_recipe_new'),
    path('dashboard/recipe/<int:id>/edit/', views.dashboard_recipe_edit, name='dashboard_recipe_edit'),
    path('dashboard/recipe/delete/', views.dashboard_recipe_delete, name='dashboard_recipe_delete'),

]

