# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-10 00:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0079_auto_20160509_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequesterAccessControlGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default=b'allow', max_length=16)),
                ('name', models.CharField(max_length=256, null=True)),
                ('is_global', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access_groups', to='crowdsourcing.Requester')),
            ],
        ),
        migrations.CreateModel(
            name='WorkerAccessControlEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='crowdsourcing.RequesterAccessControlGroup')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crowdsourcing.Worker')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='enable_blacklist',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='enable_whitelist',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='max_tasks',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='crowdsourcing.Requester'),
        ),
    ]
