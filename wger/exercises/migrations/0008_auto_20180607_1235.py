# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-07 09:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_auto_20180606_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='license_author',
            field=models.ForeignKey(default=112, help_text='If you are not the author, enter the name or source here. This is needed for some licenses e.g. the CC-BY-SA.', on_delete=django.db.models.deletion.CASCADE, to='exercises.Author'),
        ),
        migrations.AlterField(
            model_name='exerciseimage',
            name='license_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.Author'),
        ),
    ]