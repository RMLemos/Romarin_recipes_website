# Generated by Django 4.2 on 2024-03-02 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=150, null=True, unique=True),
        ),
    ]