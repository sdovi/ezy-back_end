# Generated by Django 4.2.3 on 2023-07-09 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_info_description_photo4_info_description_photo5'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='description_photo',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='info',
            old_name='description_photo2',
            new_name='photo2',
        ),
        migrations.RenameField(
            model_name='info',
            old_name='description_photo3',
            new_name='photo3',
        ),
        migrations.RenameField(
            model_name='info',
            old_name='description_photo4',
            new_name='photo4',
        ),
        migrations.RenameField(
            model_name='info',
            old_name='description_photo5',
            new_name='photo5',
        ),
    ]
