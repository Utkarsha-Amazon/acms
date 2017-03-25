# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-24 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prime',
            fields=[
                ('key_p', models.AutoField(primary_key=True, serialize=False)),
                ('day0', models.IntegerField(blank=True, null=True)),
                ('day1', models.IntegerField(blank=True, null=True)),
                ('day2', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'prime',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('key_s', models.AutoField(primary_key=True, serialize=False)),
                ('day0', models.IntegerField(blank=True, null=True)),
                ('day1', models.IntegerField(blank=True, null=True)),
                ('day2', models.IntegerField(blank=True, null=True)),
                ('day3', models.IntegerField(blank=True, null=True)),
                ('day4', models.IntegerField(blank=True, null=True)),
                ('day5', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'standard',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('locker_id', models.IntegerField(primary_key=True, serialize=False)),
                ('locker_name', models.CharField(blank=True, db_column='Locker_name', max_length=45, null=True)),
                ('city', models.CharField(blank=True, max_length=45, null=True)),
                ('state', models.CharField(blank=True, max_length=45, null=True)),
                ('pincode', models.CharField(blank=True, max_length=45, null=True)),
                ('prime_capacity', models.CharField(blank=True, max_length=45, null=True)),
                ('standard_capacity', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'table1',
                'managed': False,
            },
        ),
    ]