from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.db.models import Avg, Count, Value, IntegerField, Sum
from django.db.models.functions import Coalesce
from django.contrib import messages
import pandas as pd
import pyreadstat
from django.conf import settings
import os
from datetime import datetime
from django.db.models import Min, Max
from dateutil.relativedelta import relativedelta
from .models import Household, Individual, Education, ChildHealth, ChildHealthDetails, HouseholdProperty, HouseholdAsset, HouseholdFinance, HouseholdFoodConsumption, HouseholdNonFoodExpenditure, HouseholdIncome, HouseholdTransfer, HouseholdShock, HouseholdClimateChangeResponse




# import the second dta file to individual table
def import_dataset(request):
    if request.method == 'POST':
        try:
            file = request.FILES['file']
            file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', file.name)

            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            df, meta = pyreadstat.read_dta(file_path)
            
            column_to_field_map_hh8 = {
                'H801': 'climate_change_importance',
                'H802': 'current_effect',
                'h803': 'future_effect',
                'h804_1': 'drought_effect',
                'h804_2': 'rain_flood_effect',
                'h804_3': 'cold_winter_effect',
                'h804_4': 'frosts_effect',
                'h804_5': 'heat_wave_effect',
                'h805_o1': 'action_1',
                'h805_o2': 'action_2',
                'h805_o3': 'action_3',
                'h805_o4': 'action_4',
                'h805_o5': 'action_5',
                'h805_o6': 'action_6',
                'h805_o7': 'action_7',
                'h805_o8': 'action_8',
                'h805_o9': 'action_9',
                'h805_o10': 'action_10',
                'h805_o11': 'action_11',
                'h805_o12': 'action_12',
                'h805_o13': 'action_13',
                'h805_o14': 'action_14',
                'h805_o15': 'action_15',
            }

            for index, row in df.iterrows():
                if pd.isna(row['hhid']):
                    continue  # Skip rows with missing hhid

                # Get the Household instance
                household = Household.objects.get(hhid=row['hhid'])

                # Prepare data for HouseholdClimateChangeResponse instance
                household_climate_change_response_data = {field: row[column] for column, field in column_to_field_map_hh8.items() if column in row and not pd.isna(row[column])}

                # Create HouseholdClimateChangeResponse instance
                household_climate_change_response = HouseholdClimateChangeResponse(hhid=household, **household_climate_change_response_data)
                household_climate_change_response.save()

            os.remove(file_path)  # Delete the file after processing
            messages.success(request, "Household Climate Change Response dataset imported successfully.")
        except Exception as e:
            messages.error(request, f"Error during import: {e}")
            if os.path.exists(file_path):
                os.remove(file_path)  # Make sure to delete the file in case of error

        return redirect('home')

    return redirect('home')



# Homepage
def home(request):
    context = {}
    #return render(request, "home_page.html", context)
    # Temporary redirect to dashboard
    return render(request, "dashboard.html", context)


# Dashboard
def dashboard(request):
    context = {}
    return render(request, "dashboard.html", context)

# Dashboard Household Demographics Page
# def household_demographics(request):
#     household_instance = Household.objects.first()
#     context = {'household': household_instance}
#     return render(request, "pages/1 - household-demographics/household-demographics.html", context)


# Dashboard Household Demographics Page
class HouseholdDemographicsView(TemplateView):
    template_name = 'pages/1 - household-demographics/household-demographics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Total Number of Households
        total_households = Household.objects.count()
        # Additional information for Total Number of Households
        total_regions = Household.objects.values('oblast').distinct().count()

        # Most Common Interview Language
        common_language = Household.objects.values('lang').annotate(lang_count=Count('lang')).order_by('-lang_count').first()
        most_common_language = common_language['lang'] if common_language else 'N/A'
        
        # Interviews duration
        min_date = Household.objects.aggregate(Min('int_date'))['int_date__min']
        max_date = Household.objects.aggregate(Max('int_date'))['int_date__max']
        interview_months = relativedelta(max_date, min_date).months + 1

        # Average Household Size (assuming one Individual per Household)
        avg_household_size = Individual.objects.values('hhid').annotate(hh_size=Count('pid')).aggregate(Avg('hh_size'))['hh_size__avg']
        # Additional information for Average Household Size
        household_sizes = Individual.objects.values('hhid').annotate(hh_size=Count('pid'))
        min_household_size = household_sizes.aggregate(Min('hh_size'))['hh_size__min']
        max_household_size = household_sizes.aggregate(Max('hh_size'))['hh_size__max']
        
        # Average Response Quality Estimation
        quality_stats = Household.objects.aggregate(Avg('estim'), Min('estim'), Max('estim'))
        avg_quality = quality_stats['estim__avg']
        
        # Calculate the number of households in each region
        households_per_region = Household.objects.values('oblast').annotate(count=Count('hhid')).order_by('oblast')
        
        
        # Calculate gender distribution
        gender_distribution = Individual.objects.values('gender').annotate(count=Count('gender'))
        gender_counts = {gender.get('gender'): gender.get('count') for gender in gender_distribution}

        # Assuming 1 is Male and 2 is Female
        male_count = gender_counts.get(1, 0)
        female_count = gender_counts.get(2, 0)
        
        
        # Calculate the ethnic group distribution
        ethnicity_distribution = Individual.objects.values('ethnicity').annotate(count=Count('ethnicity')).order_by('ethnicity')

        # Preparing the data for the donut chart
        # Mapping ethnicity codes to counts. Update the indices to match the ETHNICITY_CHOICES
        ethnicity_counts = [0] * 8  # Assuming 8 ethnic groups
        for entry in ethnicity_distribution:
            if 1 <= entry['ethnicity'] <= 8:  # Adjust range based on ETHNICITY_CHOICES
                # Adjust the index to match ETHNICITY_CHOICES
                ethnicity_counts[entry['ethnicity'] - 1] = entry['count']
                
        
        
        # Exclude individuals with None as marital status
        valid_marital_status_individuals = Individual.objects.exclude(marital_status__isnull=True)
        
        # Calculate the marital status distribution
        marital_distribution = valid_marital_status_individuals.values('marital_status').annotate(count=Count('marital_status')).order_by('marital_status')

        # Preparing the data for the donut chart
        marital_counts = [0] * 6  # Adjust the size based on MARITAL_STATUS_CHOICES
        for entry in marital_distribution:
            if 1 <= entry['marital_status'] <= 6:  # Adjust range based on MARITAL_STATUS_CHOICES
                marital_counts[entry['marital_status'] - 1] = entry['count']
                
                
        # Children enrollment
        # Filter out records where 'enrolled' is None
        valid_enrollment_records = Education.objects.exclude(enrolled__isnull=True)

        # Count the number of enrolled and unenrolled children
        enrollment_counts = valid_enrollment_records.values('enrolled').annotate(count=Count('enrolled'))

        # Initialize counts
        enrolled_count = 0
        not_enrolled_count = 0

        # Extract counts from the query results
        for entry in enrollment_counts:
            if entry['enrolled'] == 1:  # 1 represents 'Yes' (enrolled)
                enrolled_count = entry['count']
            elif entry['enrolled'] == 2:  # 2 represents 'No' (unenrolled)
                not_enrolled_count = entry['count']
                
                
        # Filter out records where 'not_studying_reason' is None
        valid_unenrollment_records = Education.objects.exclude(not_studying_reason__isnull=True)

        # Count the occurrences of each unenrollment reason
        unenrollment_reason_counts = valid_unenrollment_records.values('not_studying_reason').annotate(count=Count('not_studying_reason'))

        # Calculate the total number of unenrollment reasons
        total_unenrollment_reasons = sum(item['count'] for item in unenrollment_reason_counts)

        # Calculate percentages for each reason
        unenrollment_reason_percentages = []
        for reason in range(1, 9):  # Assuming there are 8 reasons
            count = next((item['count'] for item in unenrollment_reason_counts if item['not_studying_reason'] == reason), 0)
            percentage = (count / total_unenrollment_reasons * 100) if total_unenrollment_reasons > 0 else 0
            unenrollment_reason_percentages.append(round(percentage, 2))
            
            
        # Exclude records where 'current_level' is None
        valid_education_records = Education.objects.exclude(current_level__isnull=True)

        # Count the occurrences of each education level
        education_level_counts = valid_education_records.values('current_level').annotate(count=Count('current_level'))

        # Calculate the total number of valid education level records
        total_education_records = sum(item['count'] for item in education_level_counts)

        # Calculate counts and percentages for each education level
        children_educ_data = {}
        for level in Education.CURRENT_LEVEL_CHOICES:
            level_code = level[0]
            count = next((item['count'] for item in education_level_counts if item['current_level'] == level_code), 0)
            percentage = (count / total_education_records * 100) if total_education_records > 0 else 0
            children_educ_data[level[1]] = {'count': count, 'percentage': percentage}
            
            
            
        # Aggregate language counts across first, second, and third language fields
        language_counts = Education.objects.annotate(
            first_lang=Coalesce('first_language', Value(0)),
            second_lang=Coalesce('second_language', Value(0)),
            third_lang=Coalesce('third_language', Value(0))
        ).values('first_lang', 'second_lang', 'third_lang')

        # Initialize counts (assuming 8 language choices)
        total_language_counts = [0] * 8

        # Sum the counts for each language
        for record in language_counts:
            for lang in range(1, 9):  # Assuming language choices are numbered from 1 to 8
                if record['first_lang'] == lang:
                    total_language_counts[lang - 1] += 1
                if record['second_lang'] == lang:
                    total_language_counts[lang - 1] += 1
                if record['third_lang'] == lang:
                    total_language_counts[lang - 1] += 1
                    
                    
        # Aggregate sum of each expense
        total_expenses = Education.objects.aggregate(
            total_school_fees=Sum('school_fees'),
            total_uniforms_supplies=Sum('uniforms_supplies'),
            total_non_formal_payments=Sum('non_formal_payments'),
            total_tutoring_payments=Sum('tutoring_payments'),
            total_schooling_expenditure=Sum('total_schooling_expenditure')
        )

        # Prepare the data for frontend display
        education_expenses = {
            'School Fees and Tuition': total_expenses['total_school_fees'],
            'Uniforms and Supplies': total_expenses['total_uniforms_supplies'],
            'Non-Formal Payments': total_expenses['total_non_formal_payments'],
            'Tutoring Payments': total_expenses['total_tutoring_payments'],
            'Total Schooling Expenditure': total_expenses['total_schooling_expenditure']
        }
        
        
        
        # Manual mapping of field names to display names
        display_names = {
            'medical_card': 'Having Medical Vaccination Card',
            'vaccinations': 'Received Any Vaccinations',
            'bcg_vaccination': 'Received BCG Vaccination',
            'polio_vaccine': 'Received Polio Vaccine',
        }

        health_stats = {}
        for field, display_name in display_names.items():
            # Get total count for each choice (Yes: 1, No: 2)
            yes_count = ChildHealthDetails.objects.filter(**{f'{field}': 1}).count()
            no_count = ChildHealthDetails.objects.filter(**{f'{field}': 2}).count()
            total_count = yes_count + no_count

            # Calculate percentages
            yes_percentage = (yes_count / total_count * 100) if total_count > 0 else 0
            no_percentage = (no_count / total_count * 100) if total_count > 0 else 0

            # Add to the dictionary
            health_stats[field] = {
                'display_name': display_name,
                'yes_count': yes_count,
                'no_count': no_count,
                'yes_percentage': yes_percentage,
                'no_percentage': no_percentage
            }
            
        
        
        # Count the occurrences of 'Yes' (1) and 'No' (2) for birth certificates
        certificate_counts = ChildHealthDetails.objects.values('birth_certificate').annotate(count=Count('birth_certificate'))

        # Initialize counts for 'Yes' and 'No'
        yes_count = 0
        no_count = 0

        # Extract counts from the query results
        for entry in certificate_counts:
            if entry['birth_certificate'] == 1:  # Assuming 1 represents 'Yes'
                yes_count = entry['count']
            elif entry['birth_certificate'] == 2:  # Assuming 2 represents 'No'
                no_count = entry['count']
                
                
        # Count the occurrences of 'Yes' (1) and 'No' (2) for disability or long-term illness
        disability_counts = ChildHealthDetails.objects.values('disability_illness').annotate(count=Count('disability_illness'))

        # Initialize counts for 'Yes' and 'No'
        yes_disability_count = 0
        no_disability_count = 0

        # Extract counts from the query results
        for entry in disability_counts:
            if entry['disability_illness'] == 1:  # Assuming 1 represents 'Yes'
                yes_disability_count = entry['count']
            elif entry['disability_illness'] == 2:  # Assuming 2 represents 'No'
                no_disability_count = entry['count']

        

        context['total_households'] = total_households
        context['most_common_language'] = most_common_language
        context['interview_months'] = interview_months
        context['total_regions'] = total_regions
        context['avg_household_size'] = avg_household_size
        context['min_household_size'] = min_household_size
        context['max_household_size'] = max_household_size
        context['avg_quality'] = avg_quality
        context['households_per_region'] = households_per_region
        context['gender_donut_data'] = [male_count, female_count]
        context['ethnicity_donut_data'] = ethnicity_counts
        context['marital_donut_data'] = marital_counts
        context['enrollment_pie_data'] = [enrolled_count, not_enrolled_count]
        context['unenrollment_reason_data'] = unenrollment_reason_percentages
        context['children_educ_data'] = children_educ_data
        context['languages_pie_data'] = total_language_counts
        context['education_expenses'] = education_expenses
        context['total_expenditure'] = total_expenses['total_schooling_expenditure']
        context['certificate_donut_data'] = [yes_count, no_count]
        context['health_stats'] = health_stats
        context['disability_donut_data'] = [yes_disability_count, no_disability_count]


        return context



# Economic Wellbeing Page
def economic_wellbeing(request):
    context = {}
    return render(request, "pages/2 - economic-wellbeing/economic-wellbeing.html", context)

# Housing and Amenities Page
def housing_and_amenities(request):
    context = {}
    return render(request, "pages/3 - housing-and-amenities/housing-and-amenities.html", context)

# Education and Employment Page
def education_and_employment(request):
    context = {}
    return render(request, "pages/4 - education-employment/education-employment.html", context)

# Health and Nutrition Page
def health_and_nutrition(request):
    context = {}
    return render(request, "pages/5 - health-nutrition/health-nutrition.html", context)

# Migration and Remittances Page
def migration_and_remittances(request):
    context = {}
    return render(request, "pages/6 - migration-remittances/migration-remittances.html", context)

# Shocks and Coping Mechanism Page
def shocks_and_coping_mechanism(request):
    context = {}
    return render(request, "pages/7 - family-background/family-background.html", context)

# Community Perception Page
def community_perception(request):
    context = {}
    return render(request, "pages/8 - community-perceptions/community-perceptions.html", context)