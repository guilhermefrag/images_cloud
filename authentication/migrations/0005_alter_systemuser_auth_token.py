# Generated by Django 4.1.3 on 2022-11-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_systemuser_auth_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemuser',
            name='auth_token',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]