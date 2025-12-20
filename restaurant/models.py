from django.db import models


class MenuItem(models.Model):

    CATEGORY_CHOICES = [
        ('Starter', 'Starter'),
        ('Main Course', 'Main Course'),
        ('Dessert', 'Dessert'),
        ('Drinks', 'Drinks'),
    ]

    FOOD_TYPE_CHOICES = [
        ('Veg', 'Veg'),
        ('Non-Veg', 'Non-Veg'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    food_type = models.CharField(
        max_length=10,
        choices=FOOD_TYPE_CHOICES
    )

    def __str__(self):
        return self.name
