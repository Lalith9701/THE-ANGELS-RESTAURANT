from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import MenuItem, Reservation

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
    if request.method == 'POST':
        # ── Collect form data ──────────────────────────────────────────────
        first_name = request.POST.get('first_name', '').strip()
        last_name  = request.POST.get('last_name', '').strip()
        phone      = request.POST.get('phone', '').strip()
        email      = request.POST.get('email', '').strip()
        date       = request.POST.get('date', '').strip()
        time       = request.POST.get('time', '').strip()
        guests     = request.POST.get('guests', '').strip()
        occasion   = request.POST.get('occasion', '').strip()
        notes      = request.POST.get('notes', '').strip()

        # ── Basic validation ───────────────────────────────────────────────
        if not all([first_name, phone, date, time, guests]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'restaurant/contact.html', {'form_data': request.POST})

        # ── Save to database ───────────────────────────────────────────────
        reservation = Reservation.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            date=date,
            time=time,
            guests=guests,
            occasion=occasion,
            notes=notes,
        )

        # ── Send email to admin ────────────────────────────────────────────
        subject = f"🍽️ New Reservation — {first_name} {last_name} on {date}"

        message = f"""
New table reservation received at The Angels Restaurant.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  GUEST DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Name      : {first_name} {last_name}
  Phone     : {phone}
  Email     : {email or '—'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  BOOKING DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Date      : {date}
  Time      : {time}
  Guests    : {guests}
  Occasion  : {occasion or '—'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SPECIAL REQUESTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  {notes or 'None'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Reservation ID : #{reservation.id}
  Received at    : {reservation.created_at.strftime('%d %b %Y, %I:%M %p')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Please confirm or contact the guest at your earliest convenience.

— The Angels Restaurant System
        """.strip()

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )
        except Exception:
            # Email failed but reservation is saved — don't block the user
            pass

        # ── Redirect to success page ───────────────────────────────────────
        return redirect('/contact/?success=1')

    # GET request — show form
    success = request.GET.get('success') == '1'
    return render(request, 'restaurant/contact.html', {'success': success})
