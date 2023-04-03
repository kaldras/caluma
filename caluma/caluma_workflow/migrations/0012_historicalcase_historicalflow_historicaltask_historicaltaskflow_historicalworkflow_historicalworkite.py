# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-21 08:55
from __future__ import unicode_literals

import uuid

import django.contrib.postgres.fields
import django.db.models.deletion
import localized_fields.fields.field
import simple_history.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "caluma_form",
            "0020_historicalanswer_historicalanswerdocument_historicaldocument_historicalfile_historicalform_historica",
        ),
        ("caluma_workflow", "0011_auto_20190220_1303"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalCase",
            fields=[
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("modified_at", models.DateTimeField(blank=True, editable=False)),
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
                ("history_user_id", models.CharField(max_length=150, null=True)),
                (
                    "id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                (
                    "closed_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Time when case has either been canceled or completed",
                        null=True,
                    ),
                ),
                (
                    "closed_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "closed_by_group",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            (
                                "running",
                                "Case is running and work items need to be completed.",
                            ),
                            ("completed", "Case is done."),
                            ("canceled", "Case is cancelled."),
                        ],
                        db_index=True,
                        max_length=50,
                    ),
                ),
                ("meta", models.JSONField(default=dict)),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "document",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="caluma_form.Document",
                    ),
                ),
                (
                    "workflow",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="caluma_workflow.Workflow",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical case",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalFlow",
            fields=[
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("modified_at", models.DateTimeField(blank=True, editable=False)),
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
                ("history_user_id", models.CharField(max_length=150, null=True)),
                (
                    "id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                ("next", models.TextField()),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical flow",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalTask",
            fields=[
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("modified_at", models.DateTimeField(blank=True, editable=False)),
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
                ("history_user_id", models.CharField(max_length=150, null=True)),
                ("slug", models.SlugField()),
                ("name", localized_fields.fields.field.LocalizedField(required=[])),
                (
                    "description",
                    localized_fields.fields.field.LocalizedField(
                        blank=True, null=True, required=[]
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("simple", "Task which can simply be marked as completed."),
                            (
                                "complete_workflow_form",
                                "Task to complete a defined workflow form.",
                            ),
                            (
                                "complete_task_form",
                                "Task to complete a defined task form.",
                            ),
                        ],
                        max_length=50,
                    ),
                ),
                ("meta", models.JSONField(default=dict)),
                (
                    "address_groups",
                    models.TextField(
                        blank=True,
                        help_text="Group jexl returning what group(s) derived work items will be addressed to.",
                        null=True,
                    ),
                ),
                ("is_archived", models.BooleanField(default=False)),
                (
                    "lead_time",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Time in seconds task may take to be processed.",
                        null=True,
                    ),
                ),
                (
                    "is_multiple_instance",
                    models.BooleanField(
                        default=False,
                        help_text="Allows creating multiple work items for this task using the `CreateWorkItem` mutation. If true, one work item will be created for each entry in `address_groups`.",
                    ),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "form",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="caluma_form.Form",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical task",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalTaskFlow",
            fields=[
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("modified_at", models.DateTimeField(blank=True, editable=False)),
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
                ("history_user_id", models.CharField(max_length=150, null=True)),
                (
                    "id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "flow",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="caluma_workflow.Flow",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="caluma_workflow.Task",
                    ),
                ),
                (
                    "workflow",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="caluma_workflow.Workflow",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical task flow",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalWorkflow",
            fields=[
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("modified_at", models.DateTimeField(blank=True, editable=False)),
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
                ("history_user_id", models.CharField(max_length=150, null=True)),
                ("slug", models.SlugField()),
                ("name", localized_fields.fields.field.LocalizedField(required=[])),
                (
                    "description",
                    localized_fields.fields.field.LocalizedField(
                        blank=True, null=True, required=[]
                    ),
                ),
                ("meta", models.JSONField(default=dict)),
                ("is_published", models.BooleanField(default=False)),
                ("is_archived", models.BooleanField(default=False)),
                (
                    "allow_all_forms",
                    models.BooleanField(
                        default=False,
                        help_text="Allow workflow to be started with any form",
                    ),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical workflow",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalWorkItem",
            fields=[
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("modified_at", models.DateTimeField(blank=True, editable=False)),
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
                ("history_user_id", models.CharField(max_length=150, null=True)),
                (
                    "id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                (
                    "closed_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Time when work item has either been canceled or completed",
                        null=True,
                    ),
                ),
                (
                    "closed_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "closed_by_group",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("deadline", models.DateTimeField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("ready", "Task is ready to be processed."),
                            ("completed", "Task is done."),
                            ("canceled", "Task is cancelled."),
                        ],
                        db_index=True,
                        max_length=50,
                    ),
                ),
                ("meta", models.JSONField(default=dict)),
                (
                    "addressed_groups",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=150),
                        default=list,
                        help_text="Offer work item to be processed by a group of users, such are not committed to process it though.",
                        size=None,
                    ),
                ),
                (
                    "assigned_users",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=150),
                        default=list,
                        help_text="Users responsible to undertake given work item.",
                        size=None,
                    ),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "case",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="caluma_workflow.Case",
                    ),
                ),
                (
                    "child_case",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        help_text="Defines case of a sub-workflow",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="caluma_workflow.Case",
                    ),
                ),
                (
                    "document",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="caluma_form.Document",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="caluma_workflow.Task",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical work item",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
