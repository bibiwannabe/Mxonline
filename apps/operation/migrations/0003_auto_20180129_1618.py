# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-29 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20180125_1131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userfavorite',
            options={'verbose_name': '用户收藏', 'verbose_name_plural': '用户收藏'},
        ),
    ]
