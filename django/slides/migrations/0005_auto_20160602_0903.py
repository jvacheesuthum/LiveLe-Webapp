# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0004_auto_20160602_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='current_page',
            field=models.IntegerField(default=1),
        ),
    ]
