# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-02 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursers', '0003_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.CharField(default='', max_length=20, verbose_name='课程标签'),
        ),
    ]
