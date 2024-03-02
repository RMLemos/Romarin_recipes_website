from django.db import models
from django.contrib.auth.models import User

from django.db.models import signals
from django.template.defaultfilters import slugify
from utils.images import resize_image

class Base(models.Model):
    created_at = models.DateField('Created at', auto_now_add=True)
    updated_at = models.DateField('Updated at', auto_now=True)

    class Meta:
        abstract = True

class Category(Base):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'categories'

    name = models.CharField(max_length=150)
    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True, max_length=150,
    )

    def __str__(self) -> str:
        return self.name
    

def category_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(category_pre_save, sender=Category)

class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/', blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        current_picture_name = str(self.picture.name)
        super_save = super().save(*args, **kwargs)
        picture_changed = False

        if self.picture:
            picture_changed = current_picture_name != self.picture.name

        if picture_changed:
            resize_image(self.picture, 900, True, 70)

        return super_save

def category_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(category_pre_save, sender=Category)
