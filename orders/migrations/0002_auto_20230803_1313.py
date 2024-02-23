# Generated by Django 3.1 on 2023-08-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('On the way', 'On the way'), ('Delivered', 'Delivered')], default='New', max_length=10),
        ),
    ]