from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('ready', 'Ready'),
        ('paid', 'Paid'),
    ]

    table_number = models.IntegerField()
    items = models.ManyToManyField(Item)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - Table {self.table_number}"


@receiver(m2m_changed, sender=Order.items.through)
def update_total_price(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        instance.total_price = sum(item.price for item in instance.items.all())
        instance.save()
