from django.db import models

from django.db.models import signals
from django.template.defaultfilters import slugify

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
