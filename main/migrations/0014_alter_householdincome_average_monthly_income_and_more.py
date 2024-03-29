# Generated by Django 5.0 on 2024-01-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "main",
            "0013_alter_householdclimatechangeresponse_climate_change_importance_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="householdincome",
            name="average_monthly_income",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Average Monthly Income (Soms)"
            ),
        ),
        migrations.AlterField(
            model_name="householdincome",
            name="received_income",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Yes"), (2, "No")],
                null=True,
                verbose_name="Received Any Income from This Source",
            ),
        ),
        migrations.AlterField(
            model_name="householdtransfer",
            name="average_monthly_transfer",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Average Monthly Transfer Amount (Soms)",
            ),
        ),
        migrations.AlterField(
            model_name="householdtransfer",
            name="received_transfer",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Yes"), (2, "No")],
                null=True,
                verbose_name="Received Any Income from This Transfer",
            ),
        ),
    ]
