# Generated by Django 2.2.4 on 2019-09-19 12:44
import logging

from django.db import migrations, models
from django.db.migrations import RunPython

from caluma.form.models import FormQuestion

logger = logging.getLogger(__name__)


def save_natural_keys(apps, schema_editor):
    for fq in FormQuestion.objects.all():
        FormQuestion.objects.filter(form=fq.form, question=fq.question).delete()
        fq.save()


def not_supported(apps, schema_editor):
    logger.warning("The reverse migration of this step is not supported.")


class Migration(migrations.Migration):

    dependencies = [("form", "0023_auto_20190729_1448")]

    operations = [
        migrations.AlterField(
            model_name="formquestion",
            name="id",
            field=models.CharField(
                max_length=255, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalformquestion",
            name="id",
            field=models.CharField(db_index=True, max_length=255),
        ),
        RunPython(save_natural_keys, not_supported),
    ]