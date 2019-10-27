# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-10-27 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('amount', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.TextField(help_text='The external ID of this object. Must be unique.', unique=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='area', to='consumption.Area')),
                ('tariff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tariff', to='consumption.Tariff')),
            ],
        ),
        migrations.AddField(
            model_name='consumption',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='consumption.User'),
        ),
    ]
