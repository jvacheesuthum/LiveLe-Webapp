# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 22:56
from __future__ import unicode_literals

from django.db import migrations, models
import slides.models


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0002_pdf_pdffile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='pdffile',
            field=models.FileField(upload_to=slides.models.rename),
        ),
    ]
