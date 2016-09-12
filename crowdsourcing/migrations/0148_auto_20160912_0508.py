# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-12 05:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0147_auto_20160912_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='answer_picked',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='picked_as_answer', to='crowdsourcing.Trumpify'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='tweet_picked',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='picked_as_tweet', to='crowdsourcing.Trumpify'),
        ),
    ]
