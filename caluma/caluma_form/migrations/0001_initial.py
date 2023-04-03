# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-12 12:43
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
import localized_fields.fields.field
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "created_by_group",
                    models.CharField(blank=True, max_length=150, null=True),
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
                ("value", models.JSONField()),
                ("meta", models.JSONField(default={})),
            ],
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "created_by_group",
                    models.CharField(blank=True, max_length=150, null=True),
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
                ("meta", models.JSONField(default={})),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Form",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "created_by_group",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("slug", models.SlugField(primary_key=True, serialize=False)),
                ("name", localized_fields.fields.field.LocalizedField(required=[])),
                (
                    "description",
                    localized_fields.fields.field.LocalizedField(
                        blank=True, null=True, required=[]
                    ),
                ),
                ("meta", models.JSONField(default={})),
                ("is_published", models.BooleanField(default=False)),
                ("is_archived", models.BooleanField(default=False)),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="FormQuestion",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "created_by_group",
                    models.CharField(blank=True, max_length=150, null=True),
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
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="caluma_form.Form",
                    ),
                ),
            ],
            options={"ordering": ("-sort", "id")},
        ),
        migrations.CreateModel(
            name="Option",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "created_by_group",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("slug", models.SlugField(primary_key=True, serialize=False)),
                ("label", localized_fields.fields.field.LocalizedField(required=[])),
                ("meta", models.JSONField(default={})),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "created_by_group",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("slug", models.SlugField(primary_key=True, serialize=False)),
                ("label", localized_fields.fields.field.LocalizedField(required=[])),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("checkbox", "checkbox"),
                            ("integer", "integer"),
                            ("float", "float"),
                            ("radio", "radio"),
                            ("textarea", "textarea"),
                            ("text", "text"),
                        ],
                        max_length=10,
                    ),
                ),
                ("is_required", models.TextField(default="false")),
                ("is_hidden", models.TextField(default="false")),
                ("is_archived", models.BooleanField(default=False)),
                (
                    "configuration",
                    models.JSONField(default={}),
                ),
                ("meta", models.JSONField(default={})),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="QuestionOption",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "created_by_group",
                    models.CharField(blank=True, max_length=150, null=True),
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
                (
                    "option",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="caluma_form.Option",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="caluma_form.Question",
                    ),
                ),
            ],
            options={"ordering": ("-sort", "id")},
        ),
        migrations.AddField(
            model_name="question",
            name="options",
            field=models.ManyToManyField(
                related_name="questions",
                through="caluma_form.QuestionOption",
                to="caluma_form.Option",
            ),
        ),
        migrations.AddField(
            model_name="formquestion",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="caluma_form.Question"
            ),
        ),
        migrations.AddField(
            model_name="form",
            name="questions",
            field=models.ManyToManyField(
                related_name="forms",
                through="caluma_form.FormQuestion",
                to="caluma_form.Question",
            ),
        ),
        migrations.AddField(
            model_name="document",
            name="form",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="documents",
                to="caluma_form.Form",
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="document",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="caluma_form.Document",
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="answers",
                to="caluma_form.Question",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="questionoption", unique_together=set([("option", "question")])
        ),
        migrations.AlterUniqueTogether(
            name="formquestion", unique_together=set([("form", "question")])
        ),
        migrations.AlterUniqueTogether(
            name="answer", unique_together=set([("document", "question")])
        ),
    ]
