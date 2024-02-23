# Generated by Django 4.2.1 on 2023-08-17 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_id_alter_reviewrating_id_and_more'),
        ('carts', '0004_alter_cart_id_alter_cartitem_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='variations',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]