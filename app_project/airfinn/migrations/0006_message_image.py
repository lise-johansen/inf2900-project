# Generated by Django 5.0.1 on 2024-04-28 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airfinn', '0005_remove_item_images_itemimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.URLField(default=''),
        ),
    ]
