# Generated by Django 4.2.1 on 2023-05-23 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_hotel_accommodation_hotel_contact_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='hotel/'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='hotel/'),
        ),
    ]
