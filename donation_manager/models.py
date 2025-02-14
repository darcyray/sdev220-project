from django.db import models

class Inventory(models.Model):
    # Category class using enumeration and TextChoices
    class Category(models.TextChoices):
        CLOTHES = 'CLTH', 'Clothes'
        SUPPLIES = 'SPL', 'Supplies'
        HYGIENE = 'HYG', 'Hygiene'

    item_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=Category.choices) # Ref Category class
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    # Function to better display database items/instances in Django Admin
    def __str__(self):
        return f"{self.item_name} ({self.category})"
    
class Donation(models.Model):
    donor_name = models.CharField(max_length=255, blank=True, null=True)
    donor_email = models.EmailField(blank=True, null=True)
    donated_items = models.ManyToManyField(Inventory, through="DonationItem") # Stores items in DonationItem class
    donation_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    
    # Function to better display database items/instances in Django Admin
    def __str__(self):
        return f"Donation by {self.donor_name or 'Anonymous'} on {self.donation_date.strftime('%Y-%m-%d')}"
    
class DonationItem(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE) # Ref Donation class
    inventory_item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    # Function to better display database items/instances in Django Admin
    def __str__(self):
        return f"{self.quantity}x {self.inventory_item.item_name} (Donation {self.donation.id})"
    
class Recipient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    # Function to better display database items/instances in Django Admin
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# Potential distribution model (to track outgoing items)
''' class Distribution(models.Model):
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    items_distributed = models.ManyToManyField(Inventory, through="DistributionItem")
    distribution_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Distribution to {self.recipient.first_name} on {self.distribution_date.strftime('%Y-%m-%d')}"
'''
