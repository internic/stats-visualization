# Generated by Django 5.0 on 2024-01-03 10:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_alter_childhealth_age_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="childhealthdetails",
            name="bcg_vaccination",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Yes"), (2, "No")],
                null=True,
                verbose_name="Had BCG Vaccination Against Tuberculosis",
            ),
        ),
        migrations.AlterField(
            model_name="childhealthdetails",
            name="birth_certificate",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Yes"), (2, "No"), (99, "Don't know")],
                null=True,
                verbose_name="Has Birth Certificate",
            ),
        ),
        migrations.AlterField(
            model_name="childhealthdetails",
            name="birth_place",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (2, "Issyk-kul oblast"),
                    (3, "Jalal-Abad oblast"),
                    (4, "Naryn oblast"),
                    (5, "Batken oblast"),
                    (6, "Osh oblast"),
                    (7, "Talas oblast"),
                    (8, "Chui oblast"),
                    (11, "Bishkek (Frunze)"),
                    (21, "Osh city"),
                    (66, "Outside of Kyrgyzstan"),
                ],
                null=True,
                verbose_name="Place of Birth",
            ),
        ),
        migrations.AlterField(
            model_name="childhealthdetails",
            name="disability_illness",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Yes"), (2, "No")],
                null=True,
                verbose_name="Has Disability or Long Term Limiting Illness",
            ),
        ),
        migrations.AlterField(
            model_name="childhealthdetails",
            name="doctor_consultations",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Number of Doctor Consultations in Last 12 Months",
            ),
        ),
        migrations.AlterField(
            model_name="childhealthdetails",
            name="hospital_nights",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Nights Spent in Hospital in Last 12 Months",
            ),
        ),
        migrations.AlterField(
            model_name="childhealthdetails",
            name="medical_card",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Yes"), (2, "No")],
                null=True,
                verbose_name="Has Medical Card for Vaccinations",
            ),
        ),
        migrations.AlterField(
            model_name="childhealthdetails",
            name="polio_vaccine",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Yes"), (2, "No")],
                null=True,
                verbose_name="Had Polio Vaccine",
            ),
        ),
        migrations.AlterField(
            model_name="childhealthdetails",
            name="vaccinations",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Yes"), (2, "No")],
                null=True,
                verbose_name="Had Any Vaccinations",
            ),
        ),
    ]