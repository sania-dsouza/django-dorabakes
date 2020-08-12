from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.base_page, name='base'),
    path('', views.recipes, name='recipes'),
    path('<filter>/', views.recipes_filt, name='recipes_filt'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('written_recipe/<id>', views.written_recipe, name='written-recipe'),
    path('recipes/<username>', views.recipes_user, name="recipes_user"),
]

