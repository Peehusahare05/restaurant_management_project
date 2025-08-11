from django.shortcuts import render

def menu_view(request):
    # Hardcoded list for now
    menu_items = [
        'Margherita Pizza',
        'Veggie Burger',
        'Pasta Alfredo',
        'Caesar Salad',
        'Chocolate Cake'
    ]
    return render(request, 'menu.html', {'menu_items': menu_items})
