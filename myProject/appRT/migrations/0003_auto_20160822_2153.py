# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appRT', '0002_auto_20160822_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='test',
            new_name='name',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='productionCompany',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]