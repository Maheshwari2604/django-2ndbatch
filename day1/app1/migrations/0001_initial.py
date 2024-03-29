# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-09 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(help_text='Required', max_length=250)),
                ('lastname', models.CharField(help_text='Required', max_length=250)),
                ('username', models.CharField(help_text='Required', max_length=250)),
                ('email', models.EmailField(help_text='Required', max_length=250)),
                ('contact_no', models.IntegerField(null=True)),
                ('password', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
