# Generated by Django 5.0.1 on 2024-05-06 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airfinn', '0009_remove_order_period_order_end_date_order_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default='', max_length=2000),
        ),
    ]