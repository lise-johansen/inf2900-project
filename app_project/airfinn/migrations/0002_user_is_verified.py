# Generated by Django 5.0.1 on 2024-02-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airfinn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
