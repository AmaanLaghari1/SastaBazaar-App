# Generated by Django 4.0.1 on 2023-01-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order_being_delivered_order_recieved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.CharField(blank=True, choices=[('', 'Select an option'), ('men', 'men'), ('women', 'women'), ('mob', 'mobile'), ('com', 'computer'), ('machine', 'machinery'), ('tv', 'television'), ('furn', 'furniture'), ('kitc', 'kitchen')], max_length=25, null=True),
        ),
    ]