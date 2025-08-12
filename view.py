# views.py
from django.shortcuts import render
from .models import RestaurantInfo

def homepage(request):
    info = RestaurantInfo.objects.first()
    return render(request, "homepage.html", {"phone_number": info.phone if info else None})
