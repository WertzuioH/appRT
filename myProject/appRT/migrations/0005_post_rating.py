# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appRT', '0004_auto_20160823_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
