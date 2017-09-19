# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='cashTotalSum',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='bill',
            name='cashback',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='bill',
            name='ecash_total_sum',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='bill',
            name='in_processing',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='nds18',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='bill',
            name='operationType',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='bill',
            name='taxation_type',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='bill',
            name='total_sum',
            field=models.IntegerField(default=-1),
        ),
    ]
