
from django.shortcuts import render

# Create your views here.

from .models import RestaurantInfo
from django.http import HttpResponse

def homepage(request):
    # Try to get the restaurant name from the model, fallback to a default
    name = RestaurantInfo.objects.first().name if RestaurantInfo.objects.exists() else "My Restaurant"
    html = f"""
    <html>
    <head>
        <title>Homepage</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f4f8fb; margin: 0; padding: 0; color: #222; }}
            .container {{ max-width: 600px; margin: 60px auto; background: #fff; border-radius: 10px; box-shadow: 0 2px 16px rgba(0,0,0,0.07); padding: 32px 28px; text-align: center; }}
            h1 {{ color: #3498db; margin-bottom: 18px; }}
            p {{ color: #444; font-size: 1.1rem; }}
        </style>
    </head>
    <body>
        <div class='container'>
            <h1>Welcome to {name}!</h1>
            <p>This is the homepage of your restaurant management system.</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)
