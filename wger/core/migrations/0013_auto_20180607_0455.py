# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-07 01:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20180606_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apikeyuserprofile',
            old_name='status',
            new_name='key',
        ),
        migrations.RemoveField(
            model_name='apikeyuserprofile',
            name='id',
        ),
        migrations.AlterField(
            model_name='apikeyuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='status', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]