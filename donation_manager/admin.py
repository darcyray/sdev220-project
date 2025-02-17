from django.contrib import admin

from .models import Inventory, Donation, DonationItem, Recipient

admin.site.register(Inventory, Donation, DonationItem, Recipient)
