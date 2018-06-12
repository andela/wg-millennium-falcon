# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-05 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_auto_20160921_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_author', models.CharField(blank=True, help_text='If you are not the author, enter the name or source here. This is needed for some licenses e.g. the CC-BY-SA.', max_length=50, null=True, verbose_name='Author')),
            ],
        ),
        migrations.AlterField(
            model_name='exercise',
            name='equipment',
            field=models.ManyToManyField(blank=True, to='exercises.Equipment', verbose_name='Equipment'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='muscles',
            field=models.ManyToManyField(blank=True, to='exercises.Muscle', verbose_name='Primary muscles'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='muscles_secondary',
            field=models.ManyToManyField(blank=True, related_name='secondary_muscles', to='exercises.Muscle', verbose_name='Secondary muscles'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='status',
            field=models.CharField(choices=[('1', 'Pending'), ('2', 'Accepted'), ('3', 'Declined')], default='1', editable=False, max_length=2),
        ),
        migrations.AlterField(
            model_name='exerciseimage',
            name='is_main',
            field=models.BooleanField(default=False, help_text='Tick the box if you want to set this image as the main one for the exercise (will be shown e.g. in the search). The first image is automatically marked by the system.', verbose_name='Main picture'),
        ),
        migrations.AlterField(
            model_name='exerciseimage',
            name='status',
            field=models.CharField(choices=[('1', 'Pending'), ('2', 'Accepted'), ('3', 'Declined')], default='1', editable=False, max_length=2),
        ),
        migrations.AddField(
            model_name='exercise',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='exercises.Author'),
        ),
    ]