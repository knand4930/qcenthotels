# Generated by Django 4.2.1 on 2023-05-23 06:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_hotel_breakfast_hotel_gym_hotel_parking_hotel_pool_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='accommodation',
            field=ckeditor.fields.RichTextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='contact_details',
            field=ckeditor.fields.RichTextField(blank=True, default=None, null=True),
        ),
    ]