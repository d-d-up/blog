# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-27 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcontent',
            name='views',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe4\xba\xba\xe6\x95\xb0'),
        ),
    ]