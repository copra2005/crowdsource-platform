# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-19 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0146_auto_20160909_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectiverejection',
            name='reason',
            field=models.IntegerField(choices=[(1, b'The pay is too low for the amount of work'), (2, b'The content is offensive or inappropriate'), (3, b'Other')]),
        ),
    ]