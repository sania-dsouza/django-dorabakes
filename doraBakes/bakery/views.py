import datetime
import time

from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .filters import RecipeFilter

from .forms import LoginForm, SignUpForm


# def base_page(request):
#     return HttpResponse("This is a test page")
from .models import Recipe


class LoginClass(BSModalCreateView):
    template_name = 'bakery/login.html'
    form_class = LoginForm
    success_message = 'Success: Login completed.'


@csrf_exempt
def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                time.sleep(2)
                login(request, user)
                return HttpResponseRedirect(reverse('recipes_user', args=(request.user.username, )))
            else:
                messages.error(request, "Username and password didn't match.")
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()

    return render(request, 'bakery/login.html', {'form': form})


@csrf_exempt
def signup_page(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        try:
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                email = request.POST['email']
                fname = request.POST['first_name']
                time.sleep(2)
                user = User.objects.create_user(username=username, email=email, password=password, first_name=fname)
                messages.info(request, "User created successfully!")
                return HttpResponseRedirect('/')
        except IntegrityError as e:
            messages.error(request, "Username already exists.")
        return render(request, 'bakery/signup.html', {'form': form})

    else:
        form = SignUpForm()

    return render(request, 'bakery/signup.html', {'form': form})


def written_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'bakery/written.html', {'recipe': recipe})


@csrf_exempt
def recipes(request):
    recipes = Recipe.objects.all()
    data = {
        'recipes': recipes,
    }
    return render(request, 'bakery/recipes.html', data)


@csrf_exempt
def recipes_filt(request, filter):
    if filter == "sweet":
        recipes = Recipe.objects.filter(category="SWEET")
    elif filter == "savory":
        recipes = Recipe.objects.filter(category="SAVORY")
    elif filter == "all":
        recipes = Recipe.objects.all()
    elif filter == "cooking_time":
        time_ranges = request.POST.getlist('time_range')
        rec= []
        for i in time_ranges:
            # split the range into two numbers
            r = i.split('-')
            if len(r) == 1:
                rec.append(Recipe.objects.filter(cooking_time__range=(90, 300)))
            else:
                rec.append(Recipe.objects.filter(cooking_time__range=(int(r[0]), int(r[1]))))
            return render(request, 'bakery/recipes.html', {'recipes': rec[0]})
    elif filter == "contains_egg":
        egg = request.POST.get('egg_answer')
        print(egg)
        rec = []
        if egg == "Yes":
            rec.append(Recipe.objects.filter(meat_indicator="True"))
        else:
            rec.append(Recipe.objects.filter(meat_indicator="False"))
        return render(request, 'bakery/recipes.html', {'recipes': rec[0]})

    else:
        recipes = Recipe.objects.all()

    data = {
        'recipes': recipes,
    }
    return render(request, 'bakery/recipes.html', data)


@login_required()
@csrf_exempt
def recipes_user(request, username):
    recipes = Recipe.objects.all()
    first_name = User.objects.get(username=username).first_name
    data = {
        'recipes': recipes,
        'first_name': first_name,
    }
    return render(request, 'bakery/recipes.html', data)




