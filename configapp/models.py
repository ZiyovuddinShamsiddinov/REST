from django.db import models
from django.utils.termcolors import RESET
from django.utils.text import slugify
from rest_framework.response import Response


class BaseModel(models.Model):
    created_ed=models.DateTimeField(auto_now_add=True)
    updated_ed=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True

class Actor(BaseModel):
    name = models.CharField(max_length=150)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    year = models.IntegerField()
    slug = models.SlugField(unique=True,null=True)
    genre = models.CharField(max_length=50)
    actor = models.ManyToManyField('Actor')

    def __str__(self):
        return self.name

    def save(self,**kwargs):
        if not self.slug:
            origin_slug=slugify(self.title)
            slug=origin_slug
            count=0
            while Movie.objects.filter(slug=slug).exists():
                slug=f"{slug}-{count}"
                count+=1
            self.slug=slug
        super().save(**kwargs)

