from django.core.management.base import BaseCommand
from restaurant.models import MenuItem


VEG_ITEMS = [
    # ── Soups ──
    {"name": "Tomato Basil Soup", "description": "Velvety roasted tomato soup with fresh basil and a swirl of cream.", "price": 129, "category": "Soup", "image_url": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600&q=80&auto=format&fit=crop"},
    {"name": "Sweet Corn Soup", "description": "Classic Indo-Chinese sweet corn soup with crunchy vegetables.", "price": 119, "category": "Soup", "image_url": "https://images.unsplash.com/photo-1603105037880-880cd4edfb0d?w=600&q=80&auto=format&fit=crop"},
    {"name": "Lemon Coriander Soup", "description": "Light and tangy soup with fresh coriander and a hint of lemon.", "price": 119, "category": "Soup", "image_url": "https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?w=600&q=80&auto=format&fit=crop"},
    {"name": "Mushroom Cream Soup", "description": "Rich and earthy mushroom soup finished with fresh cream.", "price": 139, "category": "Soup", "image_url": "https://images.unsplash.com/photo-1547592180-85f173990554?w=600&q=80&auto=format&fit=crop"},

    # ── Salads ──
    {"name": "Garden Fresh Salad", "description": "Crisp lettuce, cherry tomatoes, cucumber and house vinaigrette.", "price": 149, "category": "Salad", "image_url": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600&q=80&auto=format&fit=crop"},
    {"name": "Kachumber Salad", "description": "Traditional Indian chopped salad with onion, tomato, cucumber and chaat masala.", "price": 99, "category": "Salad", "image_url": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=600&q=80&auto=format&fit=crop"},
    {"name": "Roasted Beet & Feta Salad", "description": "Oven-roasted beets with crumbled feta, walnuts and honey-mustard dressing.", "price": 179, "category": "Salad", "image_url": "https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?w=600&q=80&auto=format&fit=crop"},
    {"name": "Quinoa Power Bowl", "description": "Protein-rich quinoa with avocado, roasted chickpeas and tahini drizzle.", "price": 199, "category": "Salad", "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600&q=80&auto=format&fit=crop"},

    # ── Starters (extra) ──
    {"name": "Hara Bhara Kebab", "description": "Spinach and pea patties spiced with green chillies and garam masala.", "price": 169, "category": "Starter", "image_url": "https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=600&q=80&auto=format&fit=crop"},
    {"name": "Crispy Corn", "description": "Golden fried sweet corn tossed with butter, herbs and chilli flakes.", "price": 149, "category": "Starter", "image_url": "https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=600&q=80&auto=format&fit=crop"},
    {"name": "Dahi Ke Sholay", "description": "Bread rolls stuffed with spiced hung curd and shallow fried to perfection.", "price": 159, "category": "Starter", "image_url": "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=600&q=80&auto=format&fit=crop"},

    # ── Main Course (extra) ──
    {"name": "Dal Makhani", "description": "Slow-cooked black lentils simmered overnight in butter and cream.", "price": 249, "category": "Main Course", "image_url": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=600&q=80&auto=format&fit=crop"},
    {"name": "Paneer Butter Masala", "description": "Soft paneer cubes in a rich, velvety tomato-cashew gravy.", "price": 269, "category": "Main Course", "image_url": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=600&q=80&auto=format&fit=crop"},
    {"name": "Chole Bhature", "description": "Spiced chickpea curry served with fluffy deep-fried bhature.", "price": 199, "category": "Main Course", "image_url": "https://images.unsplash.com/photo-1626132647523-66c3b3b9e4e4?w=600&q=80&auto=format&fit=crop"},
    {"name": "Kadai Paneer", "description": "Paneer and capsicum cooked in a robust kadai masala with whole spices.", "price": 259, "category": "Main Course", "image_url": "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=600&q=80&auto=format&fit=crop"},

    # ── Breads ──
    {"name": "Butter Naan", "description": "Soft leavened bread baked in a tandoor and brushed with butter.", "price": 49, "category": "Breads", "image_url": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&q=80&auto=format&fit=crop"},
    {"name": "Garlic Naan", "description": "Tandoor-baked naan topped with minced garlic and fresh coriander.", "price": 59, "category": "Breads", "image_url": "https://images.unsplash.com/photo-1574894709920-11b28e7367e3?w=600&q=80&auto=format&fit=crop"},
    {"name": "Stuffed Paratha", "description": "Whole-wheat flatbread stuffed with spiced aloo or paneer filling.", "price": 79, "category": "Breads", "image_url": "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=600&q=80&auto=format&fit=crop"},
    {"name": "Missi Roti", "description": "Gram-flour flatbread seasoned with carom seeds and green chillies.", "price": 49, "category": "Breads", "image_url": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=600&q=80&auto=format&fit=crop"},
    {"name": "Laccha Paratha", "description": "Flaky multi-layered whole-wheat paratha cooked on a tawa with ghee.", "price": 69, "category": "Breads", "image_url": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&q=80&auto=format&fit=crop"},

    # ── Rice & Biryani ──
    {"name": "Veg Dum Biryani", "description": "Fragrant basmati rice slow-cooked with seasonal vegetables and whole spices.", "price": 279, "category": "Rice & Biryani", "image_url": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=600&q=80&auto=format&fit=crop"},
    {"name": "Paneer Biryani", "description": "Aromatic biryani layered with marinated paneer and saffron-infused rice.", "price": 299, "category": "Rice & Biryani", "image_url": "https://images.unsplash.com/photo-1589302168068-964664d93dc0?w=600&q=80&auto=format&fit=crop"},
    {"name": "Jeera Rice", "description": "Steamed basmati rice tempered with cumin seeds and ghee.", "price": 149, "category": "Rice & Biryani", "image_url": "https://images.unsplash.com/photo-1536304993881-ff86e0c9b915?w=600&q=80&auto=format&fit=crop"},
    {"name": "Peas Pulao", "description": "Light and fluffy rice cooked with green peas, whole spices and mint.", "price": 169, "category": "Rice & Biryani", "image_url": "https://images.unsplash.com/photo-1596797038530-2c107229654b?w=600&q=80&auto=format&fit=crop"},

    # ── Desserts (extra) ──
    {"name": "Rasmalai", "description": "Soft cottage cheese dumplings soaked in chilled saffron-cardamom milk.", "price": 119, "category": "Dessert", "image_url": "https://images.unsplash.com/photo-1571115177098-24ec42ed204d?w=600&q=80&auto=format&fit=crop"},
    {"name": "Mango Kulfi", "description": "Traditional Indian ice cream made with condensed milk and fresh mango.", "price": 109, "category": "Dessert", "image_url": "https://images.unsplash.com/photo-1488900128323-21503983a07e?w=600&q=80&auto=format&fit=crop"},
    {"name": "Chocolate Lava Cake", "description": "Warm dark chocolate cake with a molten centre, served with vanilla ice cream.", "price": 149, "category": "Dessert", "image_url": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=600&q=80&auto=format&fit=crop"},

    # ── Drinks (extra) ──
    {"name": "Mango Lassi", "description": "Thick and creamy yoghurt drink blended with ripe Alphonso mangoes.", "price": 129, "category": "Drinks", "image_url": "https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=600&q=80&auto=format&fit=crop"},
    {"name": "Rose Sharbat", "description": "Chilled rose-flavoured drink with basil seeds and a hint of cardamom.", "price": 99, "category": "Drinks", "image_url": "https://images.unsplash.com/photo-1544145945-f90425340c7e?w=600&q=80&auto=format&fit=crop"},
    {"name": "Masala Chai", "description": "Aromatic spiced tea brewed with ginger, cardamom, cinnamon and cloves.", "price": 69, "category": "Drinks", "image_url": "https://images.unsplash.com/photo-1571934811356-5cc061b6821f?w=600&q=80&auto=format&fit=crop"},
]


NONVEG_ITEMS = [
    # ── Soups ──
    {"name": "Chicken Clear Soup", "description": "Light and nourishing clear broth with tender chicken strips and vegetables.", "price": 149, "category": "Soup", "image_url": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600&q=80&auto=format&fit=crop"},
    {"name": "Mutton Paya Soup", "description": "Traditional slow-cooked lamb trotter soup with aromatic whole spices.", "price": 179, "category": "Soup", "image_url": "https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?w=600&q=80&auto=format&fit=crop"},
    {"name": "Prawn Hot & Sour Soup", "description": "Tangy Indo-Chinese soup with juicy prawns, mushrooms and chilli vinegar.", "price": 169, "category": "Soup", "image_url": "https://images.unsplash.com/photo-1603105037880-880cd4edfb0d?w=600&q=80&auto=format&fit=crop"},

    # ── Salads ──
    {"name": "Grilled Chicken Caesar Salad", "description": "Romaine lettuce with grilled chicken, parmesan shavings and Caesar dressing.", "price": 229, "category": "Salad", "image_url": "https://images.unsplash.com/photo-1550304943-4f24f54ddde9?w=600&q=80&auto=format&fit=crop"},
    {"name": "Tandoori Chicken Salad", "description": "Sliced tandoori chicken over mixed greens with mint-yoghurt dressing.", "price": 219, "category": "Salad", "image_url": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600&q=80&auto=format&fit=crop"},
    {"name": "Prawn & Avocado Salad", "description": "Chilled prawns with creamy avocado, cherry tomatoes and lemon dressing.", "price": 249, "category": "Salad", "image_url": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=600&q=80&auto=format&fit=crop"},

    # ── Starters (extra) ──
    {"name": "Seekh Kebab", "description": "Minced lamb skewers seasoned with ginger, garlic and aromatic spices.", "price": 229, "category": "Starter", "image_url": "https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=600&q=80&auto=format&fit=crop"},
    {"name": "Fish Amritsari", "description": "Crispy batter-fried fish marinated in carom seeds and Amritsari spices.", "price": 219, "category": "Starter", "image_url": "https://images.unsplash.com/photo-1519984388953-d2406bc725e1?w=600&q=80&auto=format&fit=crop"},
    {"name": "Tandoori Prawns", "description": "Jumbo prawns marinated in yoghurt and spices, charred in the tandoor.", "price": 269, "category": "Starter", "image_url": "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=600&q=80&auto=format&fit=crop"},
    {"name": "Chicken Malai Tikka", "description": "Tender chicken marinated in cream, cheese and mild spices, grilled to perfection.", "price": 219, "category": "Starter", "image_url": "https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=600&q=80&auto=format&fit=crop"},

    # ── Main Course (extra) ──
    {"name": "Lamb Biryani Gravy", "description": "Slow-cooked lamb in a rich onion-tomato gravy with whole spices.", "price": 349, "category": "Main Course", "image_url": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=600&q=80&auto=format&fit=crop"},
    {"name": "Prawn Masala", "description": "Juicy prawns cooked in a spicy coastal masala with coconut and curry leaves.", "price": 329, "category": "Main Course", "image_url": "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=600&q=80&auto=format&fit=crop"},
    {"name": "Chicken Chettinad", "description": "Fiery South Indian chicken curry with freshly ground Chettinad spices.", "price": 319, "category": "Main Course", "image_url": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=600&q=80&auto=format&fit=crop"},
    {"name": "Fish Curry", "description": "Fresh fish fillets simmered in a tangy tamarind and coconut milk curry.", "price": 299, "category": "Main Course", "image_url": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=600&q=80&auto=format&fit=crop"},

    # ── Breads ──
    {"name": "Keema Naan", "description": "Tandoor-baked naan stuffed with spiced minced lamb and fresh herbs.", "price": 89, "category": "Breads", "image_url": "https://images.unsplash.com/photo-1574894709920-11b28e7367e3?w=600&q=80&auto=format&fit=crop"},
    {"name": "Chicken Kulcha", "description": "Soft leavened bread stuffed with minced chicken and caramelised onions.", "price": 99, "category": "Breads", "image_url": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&q=80&auto=format&fit=crop"},
    {"name": "Egg Paratha", "description": "Flaky whole-wheat paratha layered with spiced scrambled egg.", "price": 79, "category": "Breads", "image_url": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=600&q=80&auto=format&fit=crop"},

    # ── Rice & Biryani ──
    {"name": "Chicken Dum Biryani", "description": "Aromatic basmati rice slow-cooked with marinated chicken on dum.", "price": 329, "category": "Rice & Biryani", "image_url": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=600&q=80&auto=format&fit=crop"},
    {"name": "Mutton Biryani", "description": "Royal Hyderabadi-style biryani with tender mutton and caramelised onions.", "price": 369, "category": "Rice & Biryani", "image_url": "https://images.unsplash.com/photo-1589302168068-964664d93dc0?w=600&q=80&auto=format&fit=crop"},
    {"name": "Prawn Biryani", "description": "Coastal-style biryani with juicy prawns, coconut and fragrant spices.", "price": 349, "category": "Rice & Biryani", "image_url": "https://images.unsplash.com/photo-1596797038530-2c107229654b?w=600&q=80&auto=format&fit=crop"},
    {"name": "Egg Fried Rice", "description": "Wok-tossed basmati rice with eggs, spring onions and soy sauce.", "price": 199, "category": "Rice & Biryani", "image_url": "https://images.unsplash.com/photo-1536304993881-ff86e0c9b915?w=600&q=80&auto=format&fit=crop"},

    # ── Desserts (extra) ──
    {"name": "Shahi Tukda", "description": "Fried bread soaked in saffron rabri, garnished with pistachios and rose petals.", "price": 139, "category": "Dessert", "image_url": "https://images.unsplash.com/photo-1571115177098-24ec42ed204d?w=600&q=80&auto=format&fit=crop"},
    {"name": "Caramel Flan", "description": "Classic silky caramel custard with a golden caramel sauce.", "price": 129, "category": "Dessert", "image_url": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=600&q=80&auto=format&fit=crop"},

    # ── Drinks (extra) ──
    {"name": "Chicken Bone Broth", "description": "Slow-simmered chicken bone broth with ginger and black pepper.", "price": 99, "category": "Drinks", "image_url": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600&q=80&auto=format&fit=crop"},
    {"name": "Spiced Buttermilk", "description": "Chilled salted lassi with roasted cumin, ginger and fresh mint.", "price": 79, "category": "Drinks", "image_url": "https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=600&q=80&auto=format&fit=crop"},
]


class Command(BaseCommand):
    help = 'Seed new menu items with images for all categories'

    def handle(self, *args, **kwargs):
        created = 0
        skipped = 0

        all_items = [(VEG_ITEMS, 'Veg'), (NONVEG_ITEMS, 'Non-Veg')]

        for items, food_type in all_items:
            for item in items:
                obj, was_created = MenuItem.objects.get_or_create(
                    name=item['name'],
                    food_type=food_type,
                    defaults={
                        'description': item['description'],
                        'price': item['price'],
                        'category': item['category'],
                        'image_url': item['image_url'],
                    }
                )
                if was_created:
                    created += 1
                else:
                    # Update image_url if missing
                    if not obj.image_url:
                        obj.image_url = item['image_url']
                        obj.save()
                    skipped += 1

        self.stdout.write(self.style.SUCCESS(
            f'Done. Created: {created}  |  Already existed: {skipped}'
        ))
