from django.db import models


class Recipe(models.Model):
    RECIPE_CHOICES = [
        ("SWEET", "SWEET"),
        ("SAVORY", "SAVORY"),
    ]
    title = models.CharField(max_length=50, null=False, blank=False)
    category = models.CharField(max_length=20, choices=RECIPE_CHOICES, null=False, blank=False)
    link = models.URLField(null=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="./bakery/images", null=True)
    ingredients = models.TextField(null=True)
    method = models.TextField(null=True)
    meat_indicator = models.BooleanField(default=True)  # default baked good contains meat
    cooking_time = models.IntegerField()   # in minutes

    def __str__(self):
        return str(self.title)
