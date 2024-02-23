from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum

#Import Models
from carts.models import CartItem
from carts.models import Variation

@receiver(post_save, sender=CartItem)
def update_variation_stock(sender, instance, **kwargs):
    if instance.pk:
        old_cart_item = CartItem.objects.get(pk=instance.pk)
        quantity_diff = instance.quantity - old_cart_item.quantity
        for variation in instance.variations.all():
            variation.stock -= quantity_diff
            variation.save()

@receiver(post_save, sender=Variation)
def update_product_stock(sender, instance, **kwargs):
    product = instance.product
    variations = Variation.objects.filter(product=product, is_active=True)
    total_stock = variations.aggregate(total_stock=Sum('stock'))['total_stock'] or 0
    product.stock = total_stock
    product.save()
