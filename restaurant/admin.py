from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'food_type', 'category', 'price')
    list_filter = ('food_type', 'category')
