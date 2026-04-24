from django.shortcuts import render
from .models import MenuItem

CATEGORIES = [
    ('Soup', 'Soups'),
    ('Salad', 'Salads'),
    ('Starter', 'Starters'),
    ('Main Course', 'Main Course'),
    ('Breads', 'Breads'),
    ('Rice & Biryani', 'Rice & Biryani'),
    ('Dessert', 'Desserts'),
    ('Drinks', 'Drinks'),
]


def home(request):
    return render(request, 'restaurant/home.html')


def menu(request):
    veg_items = MenuItem.objects.filter(food_type='Veg').order_by('category', 'name')
    nonveg_items = MenuItem.objects.filter(food_type='Non-Veg').order_by('category', 'name')

    veg_cats = [c for c in CATEGORIES if veg_items.filter(category=c[0]).exists()]
    nonveg_cats = [c for c in CATEGORIES if nonveg_items.filter(category=c[0]).exists()]

    context = {
        'veg_items': veg_items,
        'nonveg_items': nonveg_items,
        'veg_categories': veg_cats,
        'nonveg_categories': nonveg_cats,
    }
    return render(request, 'restaurant/menu.html', context)


def contact(request):
    success = request.GET.get('success') == '1'
    return render(request, 'restaurant/contact.html', {'success': success})
