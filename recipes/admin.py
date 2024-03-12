from django.contrib import admin
from recipes.models import Category, Recipe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 'slug',
    search_fields = 'name',
    ordering = 'name',
    list_per_page = 20
    list_max_show_all = 200

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'is_published', 'author']
    list_display_links = 'title',
    search_fields = 'title', 'description',
    list_filter = 'category', 'author', 'is_published',
    list_per_page = 10
    list_editable = 'is_published',
    ordering = '-id',