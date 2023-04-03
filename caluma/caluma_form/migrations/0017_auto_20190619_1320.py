# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-19 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("caluma_form", "0016_auto_20190510_0843")]

    operations = [
        migrations.AddIndex(
            model_name="answer",
            index=models.Index(fields=["value"], name="form_answer_value_70b2d0_idx"),
        ),
        migrations.AddIndex(
            model_name="answer",
            index=models.Index(fields=["date"], name="form_answer_date_6485f0_idx"),
        ),
    ]
