# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-09-02 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourapp', '0002_auto_20210901_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tweethandl', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/pics')),
                ('tweet', models.TextField()),
            ],
        ),
    ]
