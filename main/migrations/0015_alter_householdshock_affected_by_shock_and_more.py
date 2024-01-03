# Generated by Django 5.0 on 2024-01-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0014_alter_householdincome_average_monthly_income_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="householdshock",
            name="affected_by_shock",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Yes"), (2, "No")],
                null=True,
                verbose_name="Affected by Shocks in Last 12 Months",
            ),
        ),
        migrations.AlterField(
            model_name="householdshock",
            name="extra_expenses",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Extra Expenses Due to Shock"
            ),
        ),
        migrations.AlterField(
            model_name="householdshock",
            name="income_loss",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Loss of Income Due to Shock"
            ),
        ),
    ]
