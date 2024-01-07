from django.db import models

# Create your models here.

# .dta file hh0.dta
class Household(models.Model):
    
    hhid = models.IntegerField(primary_key=True, verbose_name="Household ID")
    inter = models.IntegerField(verbose_name="Interviewer Code")
    superv = models.IntegerField(verbose_name="Supervisor Code")
    lang = models.CharField(max_length=100, verbose_name="Interview Language", null=True, blank=True)
    int_date = models.DateField(verbose_name="Interview Date", null=True, blank=True)
    int_begt = models.TimeField(verbose_name="Beginning Time of the Interview", null=True, blank=True)
    int_fint = models.TimeField(verbose_name="Completion Time of the Interview", null=True, blank=True)
    int_dur = models.CharField(max_length=5, verbose_name="Length of the Interview, hh.mm", null=True, blank=True)
    presence = models.CharField(max_length=100, verbose_name="Other Person(s) Present?", null=True, blank=True)
    estim = models.IntegerField(verbose_name="Response Quality Estimations 1-Bad to 5-Great", null=True, blank=True)
    comment = models.TextField(verbose_name="Interviewer's Comment", null=True, blank=True)
    rezult = models.CharField(max_length=255, verbose_name="Result of the Interview", null=True, blank=True)
    oblast = models.CharField(max_length=100, verbose_name="Oblast", null=True, blank=True)
    residence = models.CharField(max_length=100, verbose_name="Type of Population Point", null=True, blank=True)
    psu = models.IntegerField(verbose_name="Primary Sampling Unit", null=True, blank=True)
    soate = models.BigIntegerField(verbose_name="Population Point Code", null=True, blank=True)

    def __str__(self):
        return f"Household {self.hhid}"
    
    
# .dta file hh1a.dta
class Individual(models.Model):
    GENDER_CHOICES = [
        (1, 'Male'),
        (2, 'Female'),
    ]
    RELATIONSHIP_CHOICES = [
        (1, 'Head'),
        (2, 'Spouse/Partner'),
        (3, 'Son/Daughter'),
        (4, 'Son/Daughter-in-law'),
        (5, 'Father/Mother'),
        (6, 'Father/Mother-in-law'),
        (7, 'Sister/Brother'),
        (8, 'Grandchild'),
        (9, 'Nephew/Niece'),
        (10, 'Other relative'),
        (11, 'Other'),
    ]
    ETHNICITY_CHOICES = [
        (1, 'Kyrgyz'),
        (2, 'Uzbek'),
        (3, 'Russian'),
        (4, 'Dungan'),
        (5, 'Uigur'),
        (6, 'Tajik'),
        (7, 'Kazakh'),
        (8, 'Other'),
    ]
    MARITAL_STATUS_CHOICES = [
        (1, 'Married'),
        (2, 'Divorced'),
        (3, 'Lives together'),
        (4, 'Separated'),
        (5, 'Widowed'),
        (6, 'Single'),
    ]
    STAYED_WITH_HH_CHOICES = [
        (1, 'Yes'),
        (2, 'No, stayed somewhere else in Kyrgyzstan'),
        (3, 'No, stayed abroad'),
    ]
    NOT_STAY_REASON_CHOICES = [
        (1, 'Work'),
        (2, 'Business Trip'),
        (3, 'School/Study'),
        (4, 'Vacation'),
        (5, 'Visiting Family/Friends'),
        (6, 'In hospital'),
        (7, 'Insecurity/Violence'),
        (8, 'Other'),
    ]

    hhid = models.ForeignKey(Household, on_delete=models.CASCADE, verbose_name="Household ID")
    pid = models.IntegerField(verbose_name="Individual Code")
    gender = models.IntegerField(choices=GENDER_CHOICES, verbose_name="Gender")
    birth_month = models.IntegerField(verbose_name="Month of Birth", null=True, blank=True)
    birth_year = models.IntegerField(verbose_name="Year of Birth", null=True, blank=True)
    age = models.IntegerField(verbose_name="Age in Full Years", null=True, blank=True)
    relationship = models.IntegerField(choices=RELATIONSHIP_CHOICES, verbose_name="Relationship to the HH Head", null=True, blank=True)
    ethnicity = models.IntegerField(choices=ETHNICITY_CHOICES, verbose_name="Ethnicity", null=True, blank=True)
    marital_status = models.IntegerField(choices=MARITAL_STATUS_CHOICES, verbose_name="Marital Status", null=True, blank=True)
    spouse_id = models.IntegerField(verbose_name="ID of a Spouse/Partner", null=True, blank=True)
    stayed_with_hh = models.IntegerField(choices=STAYED_WITH_HH_CHOICES, verbose_name="Stayed with the HH Last Week?", null=True, blank=True)
    not_stay_reason = models.IntegerField(choices=NOT_STAY_REASON_CHOICES, verbose_name="Reason for Not Staying in HH", null=True, blank=True)

    # def __str__(self):
    #     return f"Individual {self.pid.id} from Household {self.hhid.id}"


# dta file hh1b.dta
class Education(models.Model):
    LANGUAGE_CHOICES = [
    (1, 'Kyrgyz'),
    (2, 'Uzbek'), 
    (3, 'Russian'),
    (4, 'English'),
    (5, 'Turkish'),
    (6, 'German'),
    (7, 'Chinese'),
    (8, 'Others'),
    ]

    ENROLLED_CHOICES = [
        (1, 'Yes'),
        (2, 'No'),
    ]
    
    NOT_STUDYING_CHOICES = [
    (1, 'Costs Too Much'),
    (2, 'Illness'),
    (3, "Doesn't Like Studying"),
    (4, 'Works to Support Family'),
    (5, 'Will Start School in 1-2 Years'),
    (6, 'Finished'),
    (7, 'Political Unrest'),
    (8, 'Other Reasons'),
    ]

    CURRENT_LEVEL_CHOICES = [
        (1, 'At a General School (Grade 1-11)'),
        (2, 'Professional Technical'),
        (3, 'Secondary Special (Schools with Specialized Curriculum)'),
        (4, 'University (Bachelor, MA)'),
    ]
    
    ATTENDING_CHOICES = [
    (1, 'Yes'),
    (2, 'No'),
]
    

    hhid = models.ForeignKey(Household, on_delete=models.CASCADE, verbose_name="Household ID")
    pid = models.ForeignKey(Individual, on_delete=models.CASCADE, verbose_name="Individual Code")
    age = models.IntegerField(verbose_name="Age in Years", null=True, blank=True)
    first_language = models.IntegerField(choices=LANGUAGE_CHOICES, verbose_name="First Language", null=True, blank=True)
    second_language = models.IntegerField(choices=LANGUAGE_CHOICES, verbose_name="Second Language", null=True, blank=True)
    third_language = models.IntegerField(choices=LANGUAGE_CHOICES, verbose_name="Third Language", null=True, blank=True)
    enrolled = models.IntegerField(choices=ENROLLED_CHOICES, verbose_name="Currently Enrolled at an Educational Institution", null=True, blank=True)
    not_studying_reason = models.IntegerField(choices=NOT_STUDYING_CHOICES, verbose_name="Reason for Not Studying", null=True, blank=True)
    current_level = models.IntegerField(choices=CURRENT_LEVEL_CHOICES, verbose_name="Current Level of Enrollment", null=True, blank=True)
    current_grade = models.IntegerField(verbose_name="Current Grade of Enrollment", null=True, blank=True)
    attending = models.IntegerField(choices=ATTENDING_CHOICES, verbose_name="Currently Attending the Institution", null=True, blank=True)
    
    school_fees = models.IntegerField(verbose_name="School Fees/Tuition Expenditure", null=True, blank=True)
    uniforms_supplies = models.IntegerField(verbose_name="Uniforms/Supplies Expenditure", null=True, blank=True)
    non_formal_payments = models.IntegerField(verbose_name="Non-Formal Payments Expenditure", null=True, blank=True)
    tutoring_payments = models.IntegerField(verbose_name="Tutoring and Payments to Staff", null=True, blank=True)
    total_schooling_expenditure = models.IntegerField(verbose_name="Total Schooling Expenditure", null=True, blank=True)
    
    homework_hours_daily = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Daily Homework Hours (Past Academic Year)", null=True, blank=True)
    help_at_home_hours_daily = models.IntegerField(verbose_name="Daily Hours Helping at Home/Business/Farm (Past Academic Year)", null=True, blank=True)
    outside_work_hours_daily = models.IntegerField(verbose_name="Daily Hours Working Outside for Money (Past Academic Year)", null=True, blank=True)
    computer_use_hours_weekly = models.IntegerField(verbose_name="Weekly Hours of Computer Use for Studies (Past Academic Year)", null=True, blank=True)
    missing_teachers = models.IntegerField(verbose_name="Number of Specific Subject Teachers Missing (Past Academic Year)", null=True, blank=True)
    
    
    def __str__(self):
        return f"Education Details for Individual {self.pid.id} from Household {self.hhid}"
    

# dta file hh1c.dta
class ChildHealth(models.Model):
    # Define the choices
    MEASURED_STATUS_CHOICES = [
        (1, 'All Measured'),
        (2, 'Partly Measured'),
        (3, 'Child not present'),
        (4, 'Parent refused'), 
        (5, 'Other')
    ]

    WEIGHING_METHOD_CHOICES = [
        (1, 'With a Parent'),
        (2, 'Alone'),
        (3, 'Not Measured'),
    ]

    YES_NO_CHOICES = [
        (1, 'Yes'),
        (2, 'No'),
    ]

    MEASUREMENT_METHOD_CHOICES = [
        (1, 'Lying Down'),
        (2, 'Standing Up'),
    ]

    ARM_CHOICES = [
        (1, 'Left'),
        (2, 'Right'),
    ]

    BREASTFED_CHOICES = [
        (1, 'Yes'),
        (2, 'No'),
        (99, "Don't Know"),
    ]
    
    hhid = models.ForeignKey(Household, on_delete=models.CASCADE, verbose_name="Household ID")
    pid = models.ForeignKey(Individual, on_delete=models.CASCADE, verbose_name="Individual Code")
    age = models.IntegerField(verbose_name="Age in Years", null=True, blank=True)
    measured_status = models.IntegerField(choices=MEASURED_STATUS_CHOICES, verbose_name="Status of Being Measured", null=True, blank=True)
    weighing_method = models.IntegerField(choices=WEIGHING_METHOD_CHOICES, verbose_name="Child Weighed Alone or With Parent", null=True, blank=True)
    child_weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Child Weight (kg.g)", null=True, blank=True)
    minimum_undressing = models.IntegerField(choices=YES_NO_CHOICES, verbose_name="Child Undressed to the Minimum", null=True, blank=True)
    parent_weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Parent Weight (kg.g)", null=True, blank=True)
    combined_weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Combined Weight of Parent and Child (kg.g)", null=True, blank=True)
    combined_undressing = models.IntegerField(choices=YES_NO_CHOICES, verbose_name="Parent and Child Undressed to the Minimum", null=True, blank=True)
    height = models.IntegerField(verbose_name="Height (cm)", null=True, blank=True)
    measurement_method = models.IntegerField(choices=MEASUREMENT_METHOD_CHOICES, verbose_name="Measurement Method", null=True, blank=True)
    arm_circumference = models.IntegerField(verbose_name="Mid-Upper Arm Circumference (mm)", null=True, blank=True)
    measured_arm = models.IntegerField(choices=ARM_CHOICES, verbose_name="Measured Arm", null=True, blank=True)
    breastfed_at_birth = models.IntegerField(choices=BREASTFED_CHOICES, verbose_name="Breastfed at Birth", null=True, blank=True)
    breastfeeding_duration = models.IntegerField(verbose_name="Breastfeeding Duration (months)", null=True, blank=True)

    def __str__(self):
        return f"Child Health Record for Individual {self.pid.id} from Household {self.hhid}"



# dta file hh1d.dta
class ChildHealthDetails(models.Model):
    # Define the choices
    YES_NO_CHOICES = [
        (1, 'Yes'),
        (2, 'No'),
    ]

    BIRTH_PLACE_CHOICES = [
        (2, 'Issyk-kul oblast'),
        (3, 'Jalal-Abad oblast'),
        (4, 'Naryn oblast'), 
        (5, 'Batken oblast'), 
        (6, 'Osh oblast'), 
        (7, 'Talas oblast'), 
        (8, 'Chui oblast'),
        (11, 'Bishkek (Frunze)'), 
        (21, 'Osh city'), 
        (66, 'Outside of Kyrgyzstan')
    ]

    YES_NO_DONT_KNOW_CHOICES = [
        (1, 'Yes'),
        (2, 'No'),
        (99, "Don't know"),
    ]
    
    
    
    hhid = models.ForeignKey(Household, on_delete=models.CASCADE, verbose_name="Household ID")
    pid = models.ForeignKey(Individual, on_delete=models.CASCADE, verbose_name="Individual Code")
    medical_card = models.IntegerField(choices=YES_NO_CHOICES, verbose_name="Has Medical Card for Vaccinations", null=True, blank=True)
    vaccinations = models.IntegerField(choices=YES_NO_CHOICES, verbose_name="Had Any Vaccinations", null=True, blank=True)
    bcg_vaccination = models.IntegerField(choices=YES_NO_CHOICES, verbose_name="Had BCG Vaccination Against Tuberculosis", null=True, blank=True)
    polio_vaccine = models.IntegerField(choices=YES_NO_CHOICES, verbose_name="Had Polio Vaccine", null=True, blank=True)
    disability_illness = models.IntegerField(choices=YES_NO_CHOICES, verbose_name="Has Disability or Long Term Limiting Illness", null=True, blank=True)
    doctor_consultations = models.IntegerField(verbose_name="Number of Doctor Consultations in Last 12 Months", null=True, blank=True)
    hospital_nights = models.IntegerField(verbose_name="Nights Spent in Hospital in Last 12 Months", null=True, blank=True)
    birth_place = models.IntegerField(choices=BIRTH_PLACE_CHOICES, verbose_name="Place of Birth", null=True, blank=True)
    birth_certificate = models.IntegerField(choices=YES_NO_DONT_KNOW_CHOICES, verbose_name="Has Birth Certificate", null=True, blank=True)
    mother_id = models.IntegerField(verbose_name="Mother's Code from HH Roster", null=True, blank=True)
    father_id = models.IntegerField(verbose_name="Father's Code from HH Roster", null=True, blank=True)
    weight = models.IntegerField( verbose_name="Weight in kg", null=True, blank=True)
    clothes_weight = models.IntegerField( verbose_name="Weight of Child's Clothes in grams", null=True, blank=True)
    height = models.IntegerField( verbose_name="Height in cm", null=True, blank=True)

    def __str__(self):
        return f"Child Health Details for Individual {self.pid.id} from Household {self.hhid}"




# dta file hh2a.dta
class HouseholdProperty(models.Model):
    hhid = models.ForeignKey(Household, on_delete=models.CASCADE, verbose_name="Household ID")
    new_hh = models.BooleanField(verbose_name="New HH Joined LiK in 2019")
    change_in_dwelling = models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (3, "Don't Know")], verbose_name="Change in Dwelling Since November 2016", null=True, blank=True)
    housing_type = models.IntegerField(choices=[(1, 'Separate Apartment'), (2, 'Separate House or Part of It'), (3, 'Other Type of Dwelling')], verbose_name="Type of Housing", null=True, blank=True)
    dwelling_acquisition = models.IntegerField(choices=[(1, 'Purchased'), (2, 'Built'), (3, 'Bartered'), (4, 'Inherited'), (5, 'Given by state/privatize'), (6, 'Rented')], verbose_name="How and When Dwelling Acquired", null=True, blank=True)
    settlement_year = models.IntegerField(verbose_name="Year of Settling in House", null=True, blank=True)
    num_rooms = models.IntegerField(verbose_name="Number of Rooms Available to Live In", null=True, blank=True)
    total_area = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Total Area of Dwelling (sq. meters)", null=True, blank=True)
    living_area = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Living Area of Dwelling (sq. meters)", null=True, blank=True)
    main_wall_material = models.IntegerField(choices=[(1, 'Mud/earth'), (2, 'Burnt bricks'), (4, 'Cement blocks/Concrete'), (5, 'Wood'), (6, 'Other')], verbose_name="Main Construction Material of the Walls", null=True, blank=True)
    main_roof_material = models.IntegerField(choices=[(1, 'Metal sheets'), (2, 'Tiles'), (3, 'Slate'), (5, 'Other')], verbose_name="Main Construction Material of the Roof", null=True, blank=True)
    main_drinking_water_source = models.IntegerField(choices=[(1, 'Public water pipe'), (2, 'Water pipe inside of the dwelling'), (3, 'Public water plumbing'), (4, 'Artesian or water well'), (5, 'Dam lake, river, lake, pounder, aryk'), (6, 'Other')], verbose_name="Main Source of Drinking Water", null=True, blank=True)
    water_source_location = models.IntegerField(choices=[(1, 'In the yard'), (2, 'On the street')], verbose_name="Location of Drinking Water Source", null=True, blank=True)
    water_source_distance = models.IntegerField(choices=[(1, 'Less than 100 m'), (2, '101-200 m'), (3, '201-500 m'), (4, '501-1000 m'), (5, 'More than 1000 m')], verbose_name="Distance to Drinking Water Source", null=True, blank=True)
    water_quality = models.IntegerField(choices=[(1, 'Excellent'), (2, 'Mostly good'), (3, 'Sometimes good, but some other times bad'), (4, 'Poor'), (5, 'Very poor')], verbose_name="Quality of Drinking Water", null=True, blank=True)
    main_heating_source = models.IntegerField(choices=[(1, 'Central heating'), (2, 'Electric heating (installed-type equipment)'), (3, 'Stove heating'), (4, 'Electric heating (transportable-type equipment)'), (5, 'Gas heating'), (6, 'No heating'), (7, 'Other')], verbose_name="Main Source of Heating", null=True, blank=True)
    heating_months = models.IntegerField(verbose_name="Months of Heating Last Winter", null=True, blank=True)
    electricity_disruption = models.IntegerField(choices=[(1, 'Never'), (2, 'Several times a year'), (3, 'Once a month'), (4, 'Once a week'), (5, 'Several times a week'), (6, 'Everyday'), (7, 'No power supply at all')], verbose_name="Frequency of Electricity Disruption", null=True, blank=True)
    main_cooking_method = models.IntegerField(choices=[(1, 'Tandyr/oven'), (2, 'Gas stove with pipe supply'), (3, 'Gas stove with balloons'), (4, 'Electric stove'), (5, 'Small electric hot plate (plitka)'), (6, 'Other')], verbose_name="Main Cooking Method", null=True, blank=True)
    bathing_facility = models.IntegerField(choices=[(1, 'Own bathroom with shower'), (2, 'Separate shower'), (3, 'Own sauna'), (4, 'Public sauna'), (5, 'Other'), (6, 'Go to relatives or friends')], verbose_name="Bathing Facility", null=True, blank=True)
    transport_station_time = models.IntegerField(choices=[(1, 'Less than 5 min'), (2, '6-15 min'), (3, '16-30 min'), (4, '31-60 min'), (5, 'More than 1 hour')], verbose_name="Time to Nearest Public Transport Station", null=True, blank=True)
    distance_to_main_road = models.IntegerField(verbose_name="Distance to Main Road (meters)", null=True, blank=True)
    distance_to_livestock_market = models.IntegerField(verbose_name="Distance to Livestock Market (meters)", null=True, blank=True)
    distance_to_town_hall = models.IntegerField(verbose_name="Distance to Town Hall (meters)", null=True, blank=True)
    distance_to_school = models.IntegerField(verbose_name="Distance to School (meters)", null=True, blank=True)
    distance_to_hospital = models.IntegerField(verbose_name="Distance to Hospital (meters)", null=True, blank=True)
    distance_to_pharmacy = models.IntegerField(verbose_name="Distance to Pharmacy (meters)", null=True, blank=True)

    def __str__(self):
        return f"Property Details for Household {self.hhid}"
    
    
# dta file hh2b.dta
class HouseholdAsset(models.Model):
    ASSET_CHOICES = [
    (1, 'Main Dwelling'), (2, 'Another House/Apartment'), (3, 'Garage'),
    (4, 'Bicycle'), (5, 'Motorcycle, Scooter'), (6, 'Car, Minibus'),
    (7, 'Tractor'), (8, 'Truck'), (9, 'Other Agricultural Machine'),
    (10, 'Refrigerator'), (11, 'Gas Stove'), (12, 'Electric Stove'),
    (13, 'Microwave'), (14, 'Air Conditioner'), (15, 'Sewing Machine'),
    (16, 'Washing Machine (Regular)'), (17, 'Washing Machine (Automated)'),
    (18, 'Vacuum Cleaner'), (19, 'Sofa'), (20, 'Wardrobe'),
    (21, 'Kitchen Furniture'), (22, 'Radio / Cassette Player'),
    (23, 'Complete Music System'), (24, 'Television'),
    (25, 'Video / DVD Player'), (26, 'Video Camera'), (27, 'Photo Camera'),
    (28, 'Digital Photo Camera'), (29, 'Personal Computer / Laptop'),
    (30, 'Tablet'), (31, 'Satellite Dish'), (32, 'Mobile Phone'),
    (33, 'Smartphone'), (34, 'Landline Phone'), (35, 'Internet Connection')
]
    ACQUISITION_CHOICES = [
        (1, 'Purchased'), (2, 'Inherited'), (3, 'Given as a Gift'), (4, 'Other Means')
    ]

    hhid = models.ForeignKey(Household, on_delete=models.CASCADE, verbose_name="Household ID")
    asset = models.IntegerField(choices=ASSET_CHOICES, verbose_name="Asset", null=True, blank=True)
    possession = models.BooleanField(verbose_name="Possession", null=True, blank=True)
    quantity = models.IntegerField(verbose_name="Quantity", null=True, blank=True)
    acquisition_method = models.IntegerField(choices=ACQUISITION_CHOICES, verbose_name="Acquisition Method", null=True, blank=True)
    acquisition_year = models.IntegerField(verbose_name="Year of Acquisition", null=True, blank=True)
    estimated_value = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Estimated Sale Value", null=True, blank=True)

    def __str__(self):
        return f"Asset Details for Household {self.hhid}"
    
    
    
# dta file hh2c.dta
class HouseholdFinance(models.Model):
    SAVINGS_INVESTMENT_CHOICES = [
    (1, 'Cash savings kept at home'),
    (2, 'Call deposits (interest-free)'),
    (3, 'Fixed-term bank deposits'),
    (4, 'Purchased foreign currency'),
    (5, 'Lending as a private loan'),
    (6, 'Other')
    ]
    
    LOAN_SOURCE_CHOICES = [
    (1, 'Private person'),
    (2, 'Commercial bank'),
    (3, 'Commercial organization'),
    (4, 'Microcredit agency'),
    (5, 'Credit union'),
    (6, 'Other sources'),
    (99, "Don't know")
    ]
    
    LOAN_PURPOSE_CHOICES = [
    (1, 'Build a house'),
    (2, 'Purchase a house/flat/land plot'),
    (3, "Cover the household's current living costs"),
    (4, 'Start business'),
    (5, 'Pay tuition fees for education'),
    (6, 'Pay for healthcare services'),
    (7, 'Purchase agricultural machinery, seeds'),
    (8, 'Purchase livestock and/or equipment related to livestock production'),
    (9, 'Cover expenses on customs (weddings, funerals etc)'),
    (10, 'Other purpose'),
    (99, "Don't know")
    ]
    
    hhid = models.ForeignKey(Household, on_delete=models.CASCADE, verbose_name="Household ID")
    savings = models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (3, "Don't Know")], verbose_name="Made Financial Savings in Last 12 Months", null=True, blank=True)
    investment_1 = models.IntegerField(choices=SAVINGS_INVESTMENT_CHOICES, verbose_name="First Investment Type", null=True, blank=True)
    investment_2 = models.IntegerField(choices=SAVINGS_INVESTMENT_CHOICES, verbose_name="Second Investment Type", null=True, blank=True)
    investment_3 = models.IntegerField(choices=SAVINGS_INVESTMENT_CHOICES, verbose_name="Third Investment Type", null=True, blank=True)
    savings_purpose = models.IntegerField(choices=[(1, 'To earn additional income'), (2, 'To insure for unexpected events'), (3, 'To accumulate to purchase real estate'), (4, 'To accumulate to purchase a durable asset'), (5, 'To accumulate for leisure'), (6, 'To spend for education or healthcare'), (7, 'Other purpose')], verbose_name="Purpose of Making Savings", null=True, blank=True)
    loan_taken = models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (99, "Don't Know")], verbose_name="Taken a Loan in Last 12 Months", null=True, blank=True)
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Original Amount of Loan", null=True, blank=True)
    loan_remaining = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Remaining Loan Amount", null=True, blank=True)
    loan_interest_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Annual Interest Rate for Loan", null=True, blank=True)
    loan_repay_date_known = models.IntegerField(choices=[(99, "Don't Know")], verbose_name="Knows Loan Repay Date", null=True, blank=True)
    loan_repay_month = models.IntegerField(verbose_name="Loan Repay Month", null=True, blank=True)
    loan_repay_year = models.IntegerField(verbose_name="Loan Repay Year", null=True, blank=True)
    loan_source = models.IntegerField(choices=LOAN_SOURCE_CHOICES, verbose_name="Loan Source", null=True, blank=True)
    loan_purpose = models.IntegerField(choices=LOAN_PURPOSE_CHOICES, verbose_name="Purpose of Loan", null=True, blank=True)
    applied_for_loan = models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (3, "Don't Know")], verbose_name="Applied for Loan", null=True, blank=True)
    received_loan_everytime = models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (3, "Don't Know")], verbose_name="Received Loan Every Time Applied", null=True, blank=True)
    loan_rejection_reason = models.IntegerField(choices=[(1, 'Lack of collateral'), (2, 'Not able to pay back'), (3, 'Credit line was exhausted'), (4, 'Other reason'), (99, "Don't Know")], verbose_name="Reason for Loan Rejection", null=True, blank=True)
    reason_for_not_applying = models.IntegerField(choices=[(1, 'Never needed any credit'), (2, 'Too risky to take credit'), (3, 'Interest rate was too high'), (4, 'No collateral'), (5, 'Religious reasons'), (6, 'Other reasons')], verbose_name="Reason for Not Applying for Loan", null=True, blank=True)

    def __str__(self):
        return f"Financial Details for Household {self.hhid}"



# dta file hh4a.dta
class HouseholdFoodConsumption(models.Model):
    FOOD_ITEM_CHOICES = [
    (1, 'Bread'), (2, 'Flour (all types)'), (3, 'Noodle products'), 
    (4, 'Rice'), (5, 'Buckwheat'), (6, 'Other cereal and beans'), 
    (7, 'Potato'), (8, 'Tomato'), (9, 'Cucumber'), 
    (10, 'Pepper'), (11, 'Eggplants'), (12, 'Carrot'), 
    (13, 'Cabbage'), (14, 'Onion'), (15, 'Other vegetables'), 
    (16, 'Apples and pear'), (17, 'Grapes'), (18, 'Bananas'), 
    (19, 'Citrus products'), (20, 'Watermelon and melon'), 
    (21, 'Other fruits and berries'), (22, 'Fresh milk'), 
    (23, 'Kefir'), (24, 'Airan'), (25, 'Sour cream'), 
    (26, 'Butter'), (27, 'Margarine'), (28, 'Cheese, cottage cheese'), 
    (29, 'Eggs'), (30, 'Fish'), (31, 'Chicken'), 
    (32, 'Beef'), (33, 'Lamb'), (34, 'Horse meat'), 
    (35, 'Pork'), (36, 'Sausages'), (37, 'Cooking oil'), 
    (38, 'Sugar'), (39, 'Sweets'), (40, 'Cookies'), 
    (41, 'Honey'), (42, 'Jam'), (43, 'Tea (black/green)'), 
    (44, 'Coffee'), (45, 'Non-alcoholic beverages'), (46, 'Beer'), 
    (47, 'Vodka'), (48, 'Cigarettes')
    ]
    UNIT_CHOICES = [
        (1, 'kg'), (2, 'litre'), (3, 'pieces'), (4, 'gram'), (5, 'pack')
    ]
    CONSUMPTION_PERIOD_CHOICES = [
        (1, 'per week'), (2, 'per month'), (3, 'per year')
    ]

    hhid = models.ForeignKey(Household, on_delete=models.CASCADE, verbose_name="Household ID")
    food_item = models.IntegerField(choices=FOOD_ITEM_CHOICES, verbose_name="Food Item", null=True, blank=True)
    quantity_bought = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Quantity of Items Bought in Last 12 Months", null=True, blank=True)
    unit_of_measurement = models.IntegerField(choices=UNIT_CHOICES, verbose_name="Units of Measurement", null=True, blank=True)
    total_expense = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Total Expenses on Items Bought (in Soms)", null=True, blank=True)
    consumption_period_bought = models.IntegerField(choices=CONSUMPTION_PERIOD_CHOICES, verbose_name="Period of Consumption for Bought Items", null=True, blank=True)
    quantity_own = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Quantity of Item Consumed from Own Production in Last 12 Months", null=True, blank=True)
    consumption_period_own = models.IntegerField(choices=CONSUMPTION_PERIOD_CHOICES, verbose_name="Period of Consumption for Own Products", null=True, blank=True)

    def __str__(self):
        return f"Food Consumption Details for Household {self.hhid}"


# dta file hh4b.dta
class HouseholdNonFoodExpenditure(models.Model):
    NON_FOOD_EXPENDITURE_CHOICES = [
        (1, 'Clothing, accessories and hats'), (2, 'Shoes'), (3, 'Fabrics'),
        (4, 'Soap, detergents'), (5, 'Personal care items and cosmetics'),
        (6, 'Medicines'), (7, 'Medical care, dental care'),
        (8, 'Cell phone fees'), (9, 'Stationary phone fees'),
        (10, 'Transportation services'), (11, 'Electricity bills'),
        (12, 'Cold water and sewage'), (13, 'Hot water'),
        (14, 'Central heating'), (15, 'Gas (natural and liquefied)'),
        (16, 'Petrol/diesel and other fuel for private vehicle'),
        (17, 'Coal and other solid fuel for heating'),
        (18, 'Taxes and social benefit plan contributions'),
        (19, 'Entertainment, recreation, eating out'),
        (20, 'Celebrations, funerals, rituals'),
        (21, 'Expenses for education, sports sections, clubs, etc.'),
        (22, 'Cable TV and Internet'),
        (23, 'Construction and maintenance/repair of housing'),
        (24, 'Maintenance and repair of vehicles and appliances'),
        (25, 'Jewellery'), (26, 'Kitchen utensils and household goods'),
        (27, 'Building materials, plumbing'), (28, 'Furniture and interior equipment'),
        (29, 'TV and radio equipment and spare parts'),
        (30, 'Electric and household appliances'),
        (31, 'Computers and office equipment'),
        (32, 'Auto vehicles'), (33, 'Other non-food goods and services')
    ]
    EXPENDITURE_PERIOD_CHOICES = [
        (1, 'per month'), (2, 'per year')
    ]

    hhid = models.ForeignKey(Household, on_delete=models.CASCADE, verbose_name="Household ID")
    non_food_item = models.IntegerField(choices=NON_FOOD_EXPENDITURE_CHOICES, verbose_name="Non-Food Expenditure Item", null=True, blank=True)
    expenditure_amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Expenditure Amount (Soms)", null=True, blank=True)
    expenditure_period = models.IntegerField(choices=EXPENDITURE_PERIOD_CHOICES, verbose_name="Expenditure Period", null=True, blank=True)

    def __str__(self):
        return f"Non-Food Expenditure Details for Household {self.hhid}"


# dta file hh5a.dta
class HouseholdIncome(models.Model):
    INCOME_SOURCE_CHOICES = [
        (1, 'Crop farming enterprises'),
        (2, 'Other agricultural enterprises (e.g., sale of livestock/poultry)'),
        (3, 'Individual entrepreneurship (excl. taxes and payments)'),
        (4, 'Other enterprises (non-agricultural)'),
        (5, 'Income from wage employment (excl. taxes and deductions)'),
        (6, 'Bonuses and other payments (excl. taxes and deductions)'),
        (7, 'Irregular one-time work'),
        (8, 'Money transfers from household members who were in migration abroad'),
        (9, 'Money transfers from abroad from persons who are not household members'),
        (10, 'Aid from persons in Kyrgyzstan who are not household members'),
        (11, 'Humanitarian assistance from NGOs, international organizations'),
        (12, 'Rents from accommodation/building(s)'),
        (13, 'Rents from land'),
        (14, 'Inheritance'),
        (15, 'Alimony'),
        (16, 'Scholarships'),
        (17, 'Other income')
    ]
    
    YES_NO_CHOICES = [
        (1, 'Yes'),
        (2, 'No'),
    ]

    hhid = models.ForeignKey(Household, on_delete=models.CASCADE, verbose_name="Household ID")
    income_source = models.IntegerField(choices=INCOME_SOURCE_CHOICES, verbose_name="Income Source", null=True, blank=True)
    received_income = models.IntegerField(choices=YES_NO_CHOICES,verbose_name="Received Any Income from This Source", null=True, blank=True)
    average_monthly_income = models.IntegerField(verbose_name="Average Monthly Income (Soms)", null=True, blank=True)

    def __str__(self):
        return f"Income Details for Household {self.hhid}"
    
    
# dta file hh5b.dta
class HouseholdTransfer(models.Model):
    TRANSFER_TYPE_CHOICES = [
        (1, 'Old-age pension (Kyrgyz pension)'),
        (2, 'Old-age pension (pensions from other countries)'),
        (3, 'Disability pension'),
        (4, 'Pension on favorable terms for special working conditions'),
        (5, "Survivor's pension"),
        (6, 'Newborn child allowance "Suiunchu"'),
        (7, 'Unified monthly allowance to low-income families and individuals, cash'),
        (8, 'Insurance benefit'),
        (9, 'Social monthly allowance (children with disabilities, heroine mothers, disabled since childhood, children of the deceased breadwinner)'),
        (10, 'Unemployment benefit'),
        (11, 'Other allowances'),
        (12, 'For public transportation'),
        (13, 'Medicaments'),
        (14, 'Maintenance of children in preschool institutions, child education'),
        (15, 'Other benefits')
    ]
    
    YES_NO_CHOICES = [
        (1, 'Yes'),
        (2, 'No'),
    ]

    hhid = models.ForeignKey(Household, on_delete=models.CASCADE, verbose_name="Household ID")
    transfer_type = models.IntegerField(choices=TRANSFER_TYPE_CHOICES, verbose_name="Transfer Type", null=True, blank=True)
    received_transfer = models.IntegerField(choices=YES_NO_CHOICES, verbose_name="Received Any Income from This Transfer", null=True, blank=True)
    average_monthly_transfer = models.IntegerField(verbose_name="Average Monthly Transfer Amount (Soms)", null=True, blank=True)

    def __str__(self):
        return f"Transfer Details for Household {self.hhid}"
    
    
# dta file hh6a.dta --> the file is corrupted
# dta file hh6b.dta --> file is ok but it is the continuation of the hh6a.dta which is corrupted


# dta file hh7.dta
class HouseholdShock(models.Model):
    SHOCK_TYPE_CHOICES = [
        (1, 'Drought'), (2, 'Too much rain or flood'), (3, 'Very cold winter'),
        (4, 'Frosts'), (5, 'Landslides'), (6, 'Pest or diseases (crops or livestock)'),
        (7, 'Fire'), (8, 'Insufficient water supply for farming or gardening'),
        (9, 'Political instability'), (10, 'Theft of assets (cash, crops, livestock)'),
        (11, 'Inability to sell agricultural and other products'), (12, 'Loss of job'),
        (13, 'Sharp fall of remittances from abroad'), (14, 'Death of a major breadwinner'),
        (15, 'Death of another HH member'), (16, 'Death of close relative, non-member of HH'),
        (17, 'Illness of a major breadwinner'), (18, 'Illness of another HH member'),
        (19, 'Divorce'), (20, 'Disputes on land issues'), (21, 'Accident'),
        (22, 'Insufficient energy supply'), (23, 'Increased violence in the neighbourhood'),
        (24, 'Border closure for the movement of people and goods'), (25, 'Forced relocation')
    ]

    SHOCK_IMPACT_CHOICES = [
        (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'No impact')
    ]
    COPING_ACTIVITY_CHOICES = [
        (1, 'Worked more'), 
        (2, 'HH member migrated'),
        (3, 'Sold assets (livestock, land, car)'),
        (4, 'Borrowed money'),
        (5, 'Other activity'),
        (6, 'Did nothing')
    ]
    
    YES_NO_CHOICES = [
        (1, 'Yes'),
        (2, 'No'),
    ]

    hhid = models.ForeignKey(Household, on_delete=models.CASCADE, verbose_name="Household ID")
    shock = models.IntegerField(choices=SHOCK_TYPE_CHOICES, verbose_name="Name of Shock", null=True, blank=True)
    affected_by_shock = models.IntegerField(choices=YES_NO_CHOICES, verbose_name="Affected by Shocks in Last 12 Months", null=True, blank=True)
    shock_impact = models.IntegerField(choices=SHOCK_IMPACT_CHOICES, verbose_name="Severity of Shock Impact", null=True, blank=True)
    extra_expenses = models.IntegerField(verbose_name="Extra Expenses Due to Shock", null=True, blank=True)
    income_loss = models.IntegerField(verbose_name="Loss of Income Due to Shock", null=True, blank=True)
    major_coping_activity_1 = models.IntegerField(choices=COPING_ACTIVITY_CHOICES, verbose_name="#1 Major Coping Activity", null=True, blank=True)
    major_coping_activity_2 = models.IntegerField(choices=COPING_ACTIVITY_CHOICES, verbose_name="#2 Major Coping Activity", null=True, blank=True)

    def __str__(self):
        return f"Shock Details for Household {self.hhid}"
    
    

# dta file hh8.dta
class HouseholdClimateChangeResponse(models.Model):
    CLIMATE_CHANGE_IMPORTANCE_CHOICES = [
        (1, 'Not at all important'), (2, 'Slightly important'), 
        (3, 'Moderately important'), (4, 'Very important'), (99, 'Do not know')
    ]
    
    
    ACTION_CHOICES = [
        (1, 'Planted different crops'), (2, 'Changed agricultural practices'), (3, 'Migration'),
        (4, 'Savings'), (5, 'Retrainings'), (6, 'Made different investments'),
        (7, 'Correct/separated sorting of waste'), (8, 'Community work day (Subbotniks)'),
        (9, 'Eating habits change (became a vegetarian)'), (10, 'Reducing the amount of plastic'),
        (11, 'Conducting regular vehicle inspections'), (12, 'Water saving'),
        (13, 'Tree planting'), (14, 'House insulation to reduce coal/wood consumption'),
        (15, 'Other measures'), (99, 'Do not know')
    ]
    
    hhid = models.ForeignKey(Household, on_delete=models.CASCADE, verbose_name="Household ID")
    climate_change_importance = models.IntegerField(choices=CLIMATE_CHANGE_IMPORTANCE_CHOICES, verbose_name="Importance of Climate Change", null=True, blank=True)
    current_effect = models.IntegerField(verbose_name="Current Effect of Climate Change (1-10)", null=True, blank=True)
    future_effect = models.IntegerField(verbose_name="Future Effect of Climate Change in Two Years (1-10)", null=True, blank=True)
    #h804_1 to h804_5
    drought_effect = models.IntegerField(verbose_name="Effect of Drought (0-10)", null=True, blank=True)
    rain_flood_effect = models.IntegerField(verbose_name="Effect of Too Much Rain or Floods (0-10)", null=True, blank=True)
    cold_winter_effect = models.IntegerField(verbose_name="Effect of Very Cold Winter (0-10)", null=True, blank=True)
    frosts_effect = models.IntegerField(verbose_name="Effect of Autumn/Spring Frosts (0-10)", null=True, blank=True)
    heat_wave_effect = models.IntegerField(verbose_name="Effect of High Temperature/Heat Wave (0-10)", null=True, blank=True)
    # h805_o1 to h805_o15
    
    action_1 = models.IntegerField(choices=ACTION_CHOICES, verbose_name="Action 1 to Reduce Climate Change Role", null=True, blank=True)
    action_2 = models.IntegerField(choices=ACTION_CHOICES, verbose_name="Action 2 to Reduce Climate Change Role", null=True, blank=True)
    action_3 = models.IntegerField(choices=ACTION_CHOICES, verbose_name="Action 3 to Reduce Climate Change Role", null=True, blank=True)
    action_4 = models.IntegerField(choices=ACTION_CHOICES, verbose_name="Action 4 to Reduce Climate Change Role", null=True, blank=True)
    action_5 = models.IntegerField(choices=ACTION_CHOICES, verbose_name="Action 5 to Reduce Climate Change Role", null=True, blank=True)
    action_6 = models.IntegerField(choices=ACTION_CHOICES, verbose_name="Action 6 to Reduce Climate Change Role", null=True, blank=True)
    action_7 = models.IntegerField(choices=ACTION_CHOICES, verbose_name="Action 7 to Reduce Climate Change Role", null=True, blank=True)
    action_8 = models.IntegerField(choices=ACTION_CHOICES, verbose_name="Action 8 to Reduce Climate Change Role", null=True, blank=True)
    action_9 = models.IntegerField(choices=ACTION_CHOICES, verbose_name="Action 9 to Reduce Climate Change Role", null=True, blank=True)
    action_10 = models.IntegerField(choices=ACTION_CHOICES, verbose_name="Action 10 to Reduce Climate Change Role", null=True, blank=True)
    action_11 = models.IntegerField(choices=ACTION_CHOICES, verbose_name="Action 11 to Reduce Climate Change Role", null=True, blank=True)
    action_12 = models.IntegerField(choices=ACTION_CHOICES, verbose_name="Action 12 to Reduce Climate Change Role", null=True, blank=True)
    action_13 = models.IntegerField(choices=ACTION_CHOICES, verbose_name="Action 13 to Reduce Climate Change Role", null=True, blank=True)
    action_14 = models.IntegerField(choices=ACTION_CHOICES, verbose_name="Action 14 to Reduce Climate Change Role", null=True, blank=True)
    action_15 = models.IntegerField(choices=ACTION_CHOICES, verbose_name="Action 15 to Reduce Climate Change Role", null=True, blank=True)
    
    def __str__(self):
        return f"Climate Change Effect for Household {self.hhid}"