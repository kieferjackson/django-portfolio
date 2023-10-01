# from .models import Product
from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "home.html", {})

def projects_all(request, *args, **kwargs):
    context = {}

    return render(request, "projects_all.html", context)

def project(request, *args, **kwargs):
    return render(request, "project.html", {})