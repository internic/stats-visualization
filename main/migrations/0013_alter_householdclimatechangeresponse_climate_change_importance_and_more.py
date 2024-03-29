# Generated by Django 5.0 on 2024-01-03 12:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "main",
            "0012_alter_householdfoodconsumption_consumption_period_bought_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="householdclimatechangeresponse",
            name="climate_change_importance",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (1, "Not at all important"),
                    (2, "Slightly important"),
                    (3, "Moderately important"),
                    (4, "Very important"),
                    (99, "Do not know"),
                ],
                null=True,
                verbose_name="Importance of Climate Change",
            ),
        ),
        migrations.AlterField(
            model_name="householdclimatechangeresponse",
            name="current_effect",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Current Effect of Climate Change (1-10)",
            ),
        ),
        migrations.AlterField(
            model_name="householdclimatechangeresponse",
            name="future_effect",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Future Effect of Climate Change in Two Years (1-10)",
            ),
        ),
        migrations.AlterField(
            model_name="householdincome",
            name="income_source",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (1, "Crop farming enterprises"),
                    (
                        2,
                        "Other agricultural enterprises (e.g., sale of livestock/poultry)",
                    ),
                    (3, "Individual entrepreneurship (excl. taxes and payments)"),
                    (4, "Other enterprises (non-agricultural)"),
                    (5, "Income from wage employment (excl. taxes and deductions)"),
                    (6, "Bonuses and other payments (excl. taxes and deductions)"),
                    (7, "Irregular one-time work"),
                    (
                        8,
                        "Money transfers from household members who were in migration abroad",
                    ),
                    (
                        9,
                        "Money transfers from abroad from persons who are not household members",
                    ),
                    (
                        10,
                        "Aid from persons in Kyrgyzstan who are not household members",
                    ),
                    (
                        11,
                        "Humanitarian assistance from NGOs, international organizations",
                    ),
                    (12, "Rents from accommodation/building(s)"),
                    (13, "Rents from land"),
                    (14, "Inheritance"),
                    (15, "Alimony"),
                    (16, "Scholarships"),
                    (17, "Other income"),
                ],
                null=True,
                verbose_name="Income Source",
            ),
        ),
        migrations.AlterField(
            model_name="householdincome",
            name="received_income",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="Received Any Income from This Source",
            ),
        ),
        migrations.AlterField(
            model_name="householdnonfoodexpenditure",
            name="expenditure_amount",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=12,
                null=True,
                verbose_name="Expenditure Amount (Soms)",
            ),
        ),
        migrations.AlterField(
            model_name="householdnonfoodexpenditure",
            name="expenditure_period",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "per month"), (2, "per year")],
                null=True,
                verbose_name="Expenditure Period",
            ),
        ),
        migrations.AlterField(
            model_name="householdnonfoodexpenditure",
            name="non_food_item",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (1, "Clothing, accessories and hats"),
                    (2, "Shoes"),
                    (3, "Fabrics"),
                    (4, "Soap, detergents"),
                    (5, "Personal care items and cosmetics"),
                    (6, "Medicines"),
                    (7, "Medical care, dental care"),
                    (8, "Cell phone fees"),
                    (9, "Stationary phone fees"),
                    (10, "Transportation services"),
                    (11, "Electricity bills"),
                    (12, "Cold water and sewage"),
                    (13, "Hot water"),
                    (14, "Central heating"),
                    (15, "Gas (natural and liquefied)"),
                    (16, "Petrol/diesel and other fuel for private vehicle"),
                    (17, "Coal and other solid fuel for heating"),
                    (18, "Taxes and social benefit plan contributions"),
                    (19, "Entertainment, recreation, eating out"),
                    (20, "Celebrations, funerals, rituals"),
                    (21, "Expenses for education, sports sections, clubs, etc."),
                    (22, "Cable TV and Internet"),
                    (23, "Construction and maintenance/repair of housing"),
                    (24, "Maintenance and repair of vehicles and appliances"),
                    (25, "Jewellery"),
                    (26, "Kitchen utensils and household goods"),
                    (27, "Building materials, plumbing"),
                    (28, "Furniture and interior equipment"),
                    (29, "TV and radio equipment and spare parts"),
                    (30, "Electric and household appliances"),
                    (31, "Computers and office equipment"),
                    (32, "Auto vehicles"),
                    (33, "Other non-food goods and services"),
                ],
                null=True,
                verbose_name="Non-Food Expenditure Item",
            ),
        ),
        migrations.AlterField(
            model_name="householdshock",
            name="affected_by_shock",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="Affected by Shocks in Last 12 Months",
            ),
        ),
        migrations.AlterField(
            model_name="householdshock",
            name="shock",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (1, "Drought"),
                    (2, "Too much rain or flood"),
                    (3, "Very cold winter"),
                    (4, "Frosts"),
                    (5, "Landslides"),
                    (6, "Pest or diseases (crops or livestock)"),
                    (7, "Fire"),
                    (8, "Insufficient water supply for farming or gardening"),
                    (9, "Political instability"),
                    (10, "Theft of assets (cash, crops, livestock)"),
                    (11, "Inability to sell agricultural and other products"),
                    (12, "Loss of job"),
                    (13, "Sharp fall of remittances from abroad"),
                    (14, "Death of a major breadwinner"),
                    (15, "Death of another HH member"),
                    (16, "Death of close relative, non-member of HH"),
                    (17, "Illness of a major breadwinner"),
                    (18, "Illness of another HH member"),
                    (19, "Divorce"),
                    (20, "Disputes on land issues"),
                    (21, "Accident"),
                    (22, "Insufficient energy supply"),
                    (23, "Increased violence in the neighbourhood"),
                    (24, "Border closure for the movement of people and goods"),
                    (25, "Forced relocation"),
                ],
                null=True,
                verbose_name="Name of Shock",
            ),
        ),
        migrations.AlterField(
            model_name="householdshock",
            name="shock_impact",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "High"), (2, "Medium"), (3, "Low"), (4, "No impact")],
                null=True,
                verbose_name="Severity of Shock Impact",
            ),
        ),
        migrations.AlterField(
            model_name="householdtransfer",
            name="received_transfer",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="Received Any Income from This Transfer",
            ),
        ),
        migrations.AlterField(
            model_name="householdtransfer",
            name="transfer_type",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (1, "Old-age pension (Kyrgyz pension)"),
                    (2, "Old-age pension (pensions from other countries)"),
                    (3, "Disability pension"),
                    (4, "Pension on favorable terms for special working conditions"),
                    (5, "Survivor's pension"),
                    (6, 'Newborn child allowance "Suiunchu"'),
                    (
                        7,
                        "Unified monthly allowance to low-income families and individuals, cash",
                    ),
                    (8, "Insurance benefit"),
                    (
                        9,
                        "Social monthly allowance (children with disabilities, heroine mothers, disabled since childhood, children of the deceased breadwinner)",
                    ),
                    (10, "Unemployment benefit"),
                    (11, "Other allowances"),
                    (12, "For public transportation"),
                    (13, "Medicaments"),
                    (
                        14,
                        "Maintenance of children in preschool institutions, child education",
                    ),
                    (15, "Other benefits"),
                ],
                null=True,
                verbose_name="Transfer Type",
            ),
        ),
    ]
