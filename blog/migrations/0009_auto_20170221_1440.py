# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_page_top_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='top_image',
            new_name='top_image_left',
        ),
        migrations.AddField(
            model_name='page',
            name='top_image_right',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
