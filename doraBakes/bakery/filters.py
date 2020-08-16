from .models import Recipe
import django_filters


class RecipeFilter(django_filters.FilterSet):
    class Meta:
        model = Recipe
        fields = ['title', 'category', 'link', 'description', 'img_link', 'ingredients', 'method', 'meat_indicator', 'cooking_time']