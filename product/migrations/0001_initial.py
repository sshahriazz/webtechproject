# Generated by Django 3.0.4 on 2020-03-14 06:06

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_description', models.TextField(max_length=5000)),
                ('item_regular_price', models.IntegerField()),
                ('item_quantity', models.IntegerField(default=0)),
                ('item_discounted_price', models.IntegerField()),
                ('item_image1', models.ImageField(upload_to=product.models.upload_location)),
                ('item_image2', models.ImageField(upload_to=product.models.upload_location)),
                ('item_image3', models.ImageField(upload_to=product.models.upload_location)),
                ('item_created', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('item_updated', models.DateTimeField(auto_now_add=True, verbose_name='date updated')),
                ('item_slug', models.SlugField(blank=True, unique=True)),
                ('item_from_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.ShopsData')),
            ],
            options={
                'verbose_name_plural': 'Items',
            },
        ),
    ]
