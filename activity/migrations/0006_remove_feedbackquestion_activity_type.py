# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 15:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0005_remove_feedbackanswer_activity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackquestion',
            name='activity_type',
        ),
    ]
