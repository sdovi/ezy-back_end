# Generated by Django 4.2.2 on 2023-06-21 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_info_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='photo',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]