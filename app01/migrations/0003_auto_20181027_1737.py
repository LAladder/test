# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-27 09:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_press'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Press',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
