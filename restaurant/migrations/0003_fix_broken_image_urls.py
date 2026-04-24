from django.db import migrations


def fix_broken_urls(apps, schema_editor):
    MenuItem = apps.get_model('restaurant', 'MenuItem')
    fixes = [
        ('Jeera Rice',     'Veg',     'https://images.unsplash.com/photo-1645177628172-a94c1f96e6db?w=600&q=80&auto=format&fit=crop'),
        ('Chole Bhature',  'Veg',     'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=600&q=80&auto=format&fit=crop'),
        ('Egg Fried Rice', 'Non-Veg', 'https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=600&q=80&auto=format&fit=crop'),
    ]
    for name, food_type, url in fixes:
        MenuItem.objects.filter(name=name, food_type=food_type).update(image_url=url)


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_add_categories_and_image_url'),
    ]

    operations = [
        migrations.RunPython(fix_broken_urls, migrations.RunPython.noop),
    ]
