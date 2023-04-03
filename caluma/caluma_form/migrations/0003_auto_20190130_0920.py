# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-30 09:20
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("caluma_form", "0002_auto_20181221_1517")]

    operations = [
        migrations.CreateModel(
            name="AnswerDocument",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "created_by_group",
                    models.CharField(
                        blank=True, db_index=True, max_length=150, null=True
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "sort",
                    models.PositiveIntegerField(
                        db_index=True, default=0, editable=False
                    ),
                ),
            ],
            options={"ordering": ("-sort", "id")},
        ),
        migrations.AddField(
            model_name="document",
            name="family",
            field=models.UUIDField(
                db_index=True,
                default=uuid.uuid4,
                help_text="Family id which document belongs too.",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="question",
            name="row_form",
            field=models.ForeignKey(
                blank=True,
                help_text="One row of table is represented by this form",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="caluma_form.Form",
            ),
        ),
        migrations.AlterField(
            model_name="answer",
            name="value",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="question",
            name="type",
            field=models.CharField(
                choices=[
                    ("checkbox", "checkbox"),
                    ("integer", "integer"),
                    ("float", "float"),
                    ("radio", "radio"),
                    ("textarea", "textarea"),
                    ("text", "text"),
                    ("table", "table"),
                ],
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="answerdocument",
            name="answer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="caluma_form.Answer"
            ),
        ),
        migrations.AddField(
            model_name="answerdocument",
            name="document",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="caluma_form.Document"
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="documents",
            field=models.ManyToManyField(
                related_name="_answer_documents_+",
                through="caluma_form.AnswerDocument",
                to="caluma_form.Document",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="answerdocument", unique_together=set([("answer", "document")])
        ),
    ]
