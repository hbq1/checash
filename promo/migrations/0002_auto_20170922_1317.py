# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='promos', to='items.Item'),
        ),
    ]