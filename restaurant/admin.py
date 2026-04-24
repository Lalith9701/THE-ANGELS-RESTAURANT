from django.contrib import admin
from .models import MenuItem, Reservation


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'food_type', 'category', 'price')
    list_filter = ('food_type', 'category')
    search_fields = ('name',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display  = ('first_name', 'last_name', 'phone', 'email', 'date', 'time', 'guests', 'occasion', 'status', 'created_at')
    list_filter   = ('status', 'date', 'occasion')
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    ordering      = ('-created_at',)
    readonly_fields = ('created_at',)

    # Allow admin to change status directly from the list view
    list_editable = ('status',)

    fieldsets = (
        ('Guest Info', {
            'fields': ('first_name', 'last_name', 'phone', 'email')
        }),
        ('Booking Details', {
            'fields': ('date', 'time', 'guests', 'occasion', 'notes')
        }),
        ('Status', {
            'fields': ('status', 'created_at')
        }),
    )
