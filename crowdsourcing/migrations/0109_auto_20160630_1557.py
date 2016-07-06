# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-30 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0108_remove_templateitem_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='crowdsourcing.Region'),
        ),
    ]
