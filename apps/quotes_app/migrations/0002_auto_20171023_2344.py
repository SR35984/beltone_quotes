# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-23 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0001_initial'),
        ('quotes_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='author',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='title',
            new_name='quoted_by',
        ),
        migrations.AddField(
            model_name='quote',
            name='favorited_by',
            field=models.ManyToManyField(related_name='favorites', to='login_reg_app.User'),
        ),
        migrations.AddField(
            model_name='quote',
            name='posted_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posted_quotes', to='login_reg_app.User'),
            preserve_default=False,
        ),
    ]