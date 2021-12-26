from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as django_logout

def index(request):
    return redirect("/")

def signup(request):
    if request.method == "GET":
        return render(request, 'accounts/signup.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username):
            user = User.objects.create_superuser(username, None, password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect("/")

def signin(request):
    if request.method == "GET":
        return render(request, 'accounts/signin.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect("/")

def logout(request):
    django_logout(request)
    return redirect("/")