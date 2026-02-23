#views page
from django.shortcuts import render
from .models import MenuItem

def home(request):
    return render(request, 'restaurant/home.html')

def menu(request):
    veg_items = MenuItem.objects.filter(food_type='Veg')
    nonveg_items = MenuItem.objects.filter(food_type='Non-Veg')

    context = {
        'veg_items': veg_items,
        'nonveg_items': nonveg_items,
    }
    return render(request, 'restaurant/menu.html', context)

def contact(request):
    return render(request, 'restaurant/contact.html')
