# Generated by Django 4.2.1 on 2023-05-24 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_rename_offer1_package_short_remove_package_offer2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelcontact',
            old_name='state',
            new_name='city',
        ),
        migrations.AddField(
            model_name='hotelcontact',
            name='state_hotel',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]