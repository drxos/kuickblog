# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 08:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0004_auto_20160112_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='user',
        ),
        migrations.RemoveField(
            model_name='editor',
            name='author_ptr',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Editor',
        ),
    ]
