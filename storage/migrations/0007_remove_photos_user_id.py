# Generated by Django 4.1.3 on 2022-11-28 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0006_photos_user_id_alter_photos_photo_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='user_id',
        ),
    ]
