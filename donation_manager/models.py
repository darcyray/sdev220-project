from django.db import models

class Inventory(models.Model):
    item_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)
