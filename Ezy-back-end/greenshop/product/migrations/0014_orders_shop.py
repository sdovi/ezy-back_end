# Generated by Django 4.1.3 on 2023-07-18 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_orders_alter_info_photo_alter_info_photo2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='shop',
            field=models.TextField(default=1, verbose_name='Продукт'),
            preserve_default=False,
        ),
    ]