# Generated by Django 4.0.4 on 2022-06-11 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0002_place_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='range',
            field=models.IntegerField(null=True),
        ),
    ]