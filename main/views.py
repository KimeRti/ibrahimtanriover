from django.shortcuts import render
from .models import *


def home(request):
    image = photos.objects.all()
    data = {
        'image': image
    }
    return render(request, "index.html",data)