# Generated by Django 3.0.4 on 2020-03-14 17:11

import accounts.models
from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('image', models.ImageField(upload_to=accounts.models.upload_location)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date_joined')),
                ('city', models.CharField(max_length=255)),
                ('address', models.TextField(max_length=255)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last_login')),
                ('is_shop_owner', models.BooleanField(default=False)),
                ('is_bearer', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('user_slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
