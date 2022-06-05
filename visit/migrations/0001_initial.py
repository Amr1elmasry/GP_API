# Generated by Django 4.0.4 on 2022-05-27 02:36

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=5000, null=True)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=1000), default=list, size=3)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('name_arabic', models.CharField(max_length=100, null=True)),
                ('description_arabic', models.TextField(max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=5000, null=True)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=1000), default=list, size=3)),
                ('voice_over', models.URLField(max_length=1000, null=True)),
                ('name_arabic', models.CharField(max_length=100, null=True)),
                ('description_arabic', models.TextField(max_length=5000, null=True)),
                ('voice_over_arabic', models.URLField(max_length=1000, null=True)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Place', to='visit.place')),
            ],
        ),
    ]
