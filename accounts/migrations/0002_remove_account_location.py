# Generated by Django 3.0.4 on 2020-03-14 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='location',
        ),
    ]
