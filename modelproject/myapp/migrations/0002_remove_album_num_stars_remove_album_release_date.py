# Generated by Django 4.0.6 on 2022-07-16 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='num_stars',
        ),
        migrations.RemoveField(
            model_name='album',
            name='release_date',
        ),
    ]
