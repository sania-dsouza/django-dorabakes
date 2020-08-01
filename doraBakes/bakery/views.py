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

from .forms import LoginForm, SignUpForm


# def base_page(request):
#     return HttpResponse("This is a test page")


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
                return HttpResponseRedirect(reverse('recipes_user', args=(request.user.username,)))
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
                return render(request, 'bakery/recipes.html')
        except IntegrityError as e:
            messages.error(request, "Username already exists.")
            return render(request, 'bakery/signup.html', {'form': form})

    else:
        form = SignUpForm()

    return render(request, 'bakery/signup.html', {'form': form})


@csrf_protect
def recipes(request):
    return render(request, 'bakery/recipes.html')


@csrf_protect
def recipes_user(request, username):
    return HttpResponse("Recipes of the logged in user")
