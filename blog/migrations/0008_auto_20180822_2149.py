# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-22 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180822_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_enable',
            field=models.BooleanField(default=True),
        ),
    ]
