# Generated by Django 4.1.7 on 2023-03-04 06:02

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('txt', models.TextField(blank=True, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='aboutcategory/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AddBudget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('udpate_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AddFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('udpate_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=600, null=True, unique=True)),
                ('caption', models.TextField(blank=True, null=True)),
                ('meta_title', models.TextField(blank=True, null=True)),
                ('meta_keyword', models.TextField(blank=True, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog/')),
                ('txt', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('view', models.PositiveBigIntegerField(default=0)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('txt', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='blogcategory/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('udpate_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('txt', models.TextField(blank=True, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='eventcategory/')),
                ('img', models.ImageField(blank=True, null=True, upload_to='eventcategory/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='gallerycategory/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('udpate_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('udpate_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OccasionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OfferSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='slider/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SimilarCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('udpate_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='slider/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('udpate_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('postion', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='testimonial/')),
                ('txt', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.PositiveBigIntegerField(blank=True, null=True)),
                ('price_increase', models.PositiveBigIntegerField(blank=True, null=True)),
                ('agent_price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('total_budget', models.PositiveBigIntegerField(blank=True, null=True)),
                ('agent', models.PositiveBigIntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('veg_plate', models.CharField(blank=True, max_length=200, null=True)),
                ('non_veg_plate', models.CharField(blank=True, max_length=200, null=True)),
                ('min_capacity', models.CharField(blank=True, max_length=200, null=True)),
                ('max_capacity', models.CharField(blank=True, max_length=200, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=200, null=True)),
                ('meta_keyword', models.CharField(blank=True, max_length=200, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='venue/')),
                ('venue_policy', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('alcohol', models.TextField(blank=True, null=True)),
                ('food', models.TextField(blank=True, null=True)),
                ('decoration', models.TextField(blank=True, null=True)),
                ('advance', models.CharField(blank=True, max_length=200, null=True)),
                ('cancelecation_charge', models.CharField(blank=True, max_length=200, null=True)),
                ('parking_at', models.CharField(blank=True, max_length=200, null=True)),
                ('taxes_charge', models.CharField(blank=True, max_length=200, null=True)),
                ('check_in', models.DateField(blank=True, null=True)),
                ('check_out', models.DateField(blank=True, null=True)),
                ('start_time_morning', models.TimeField(blank=True, null=True)),
                ('end_time_morning', models.TimeField(blank=True, null=True)),
                ('start_time_evening', models.TimeField(blank=True, null=True)),
                ('end_time_evening', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VenuImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.ImageField(upload_to='venu/images/')),
                ('venu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.venu')),
            ],
        ),
        migrations.AddField(
            model_name='venu',
            name='cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.venucategory'),
        ),
        migrations.AddField(
            model_name='venu',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.city'),
        ),
        migrations.AddField(
            model_name='venu',
            name='facility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.addfacility'),
        ),
        migrations.AddField(
            model_name='venu',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.hotel'),
        ),
        migrations.AddField(
            model_name='venu',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.location'),
        ),
        migrations.AddField(
            model_name='venu',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.state'),
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_id', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('children', models.PositiveSmallIntegerField(default=0)),
                ('guest', models.PositiveSmallIntegerField(default=1)),
                ('room', models.PositiveSmallIntegerField(default=1)),
                ('check_in', models.DateField(blank=True, null=True)),
                ('check_out', models.DateField(blank=True, null=True)),
                ('price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('user_type', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, choices=[('pending', 'pending'), ('accepted', 'accepted'), ('cancelled', 'cancelled'), ('completed', 'completed')], default='pending', max_length=200, null=True)),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.venu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.state'),
        ),
        migrations.CreateModel(
            name='GalleryVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('lnk', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='galleryvideo/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.gallerycategory')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='galleryimage/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.gallerycategory')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=600, null=True, unique=True)),
                ('caption', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog/')),
                ('txt', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.eventcategory')),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.blog')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.blogcategory'),
        ),
    ]
