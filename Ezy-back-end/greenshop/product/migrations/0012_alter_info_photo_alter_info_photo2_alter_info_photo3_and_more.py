# Generated by Django 4.2.3 on 2023-07-10 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_rename_description_photo_info_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='photo',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='info',
            name='photo2',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='info',
            name='photo3',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='info',
            name='photo4',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='info',
            name='photo5',
            field=models.CharField(max_length=1000),
        ),
    ]