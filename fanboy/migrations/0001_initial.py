# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BriarPipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=20)),
                ('groupsize', models.IntegerField()),
                ('craftsman', models.CharField(max_length=40)),
            ],
        ),
    ]
