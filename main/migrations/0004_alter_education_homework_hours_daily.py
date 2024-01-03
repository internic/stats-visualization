# Generated by Django 5.0 on 2024-01-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_alter_education_age_alter_education_enrolled"),
    ]

    operations = [
        migrations.AlterField(
            model_name="education",
            name="homework_hours_daily",
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name="Daily Homework Hours (Past Academic Year)",
            ),
        ),
    ]