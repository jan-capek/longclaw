# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-07 20:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_basketitem_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basketitem',
            old_name='product',
            new_name='variant',
        ),
    ]
