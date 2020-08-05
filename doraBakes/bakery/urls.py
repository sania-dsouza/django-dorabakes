from django.urls import path

from . import views

urlpatterns = [
    # path('', views.base_page, name='base'),
    path('', views.recipes, name='recipes'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('written-recipe/', views.written_recipe, name='written-recipe'),
    path('recipes/<username>', views.recipes_user, name="recipes_user"),
]

