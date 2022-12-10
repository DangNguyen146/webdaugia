from django.shortcuts import render
from django.contrib.auth.models import User


def Home(request):
    return render(request, 'homepage.html')
