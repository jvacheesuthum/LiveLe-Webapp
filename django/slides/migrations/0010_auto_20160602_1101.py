# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0009_auto_20160602_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='lecture',
            field=models.CharField(max_length=50),
        ),
    ]
