from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd
import pyreadstat
from django.conf import settings
import os
from datetime import datetime
from .models import Household, Individual, Education, ChildHealth, ChildHealthDetails, HouseholdProperty, HouseholdAsset, HouseholdFinance, HouseholdFoodConsumption, HouseholdNonFoodExpenditure, HouseholdIncome, HouseholdTransfer, HouseholdShock, HouseholdClimateChangeResponse


# import dta files to database
# def import_dataset(request):
#     if request.method == 'POST':
#         try:
#             file = request.FILES['file']
#             file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', file.name)

#             with open(file_path, 'wb+') as destination:
#                 for chunk in file.chunks():
#                     destination.write(chunk)

#             df, meta = pyreadstat.read_dta(file_path)

#             for index, row in df.iterrows():
#                 # Handle the date format conversion
#                 if not pd.isna(row['int_date']):
#                     row['int_date'] = datetime.strptime(row['int_date'], '%d.%m.%Y').strftime('%Y-%m-%d')
                
#                 # Create a dictionary with NaN checks
#                 row_data = {field: row[field] if not pd.isna(row[field]) else None for field in row.index}
                
#                 # Create and save the Household object
#                 household = Household(**row_data)
#                 household.save()
                

#             os.remove(file_path)  # Delete the file after processing
#             messages.success(request, "Dataset imported successfully.")
#         except Exception as e:
#             messages.error(request, f"Error during import: {e}")
#             if os.path.exists(file_path):
#                 os.remove(file_path)  # Make sure to delete the file in case of error

#         return redirect('home')

#     return redirect('home')



# Import csv files to database
# def import_dataset(request):
#     if request.method == 'POST':
#         try:
#             file = request.FILES['file']
#             file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', file.name)

#             with open(file_path, 'wb+') as destination:
#                 for chunk in file.chunks():
#                     destination.write(chunk)

#             # Read CSV file instead of .dta
#             df = pd.read_csv(file_path)

#             for index, row in df.iterrows():
#                 # Handle the date format conversion
#                 if not pd.isna(row['int_date']):
#                     row['int_date'] = pd.to_datetime(row['int_date']).strftime('%Y-%m-%d')
                
#                 # Create a dictionary with NaN checks
#                 row_data = {field: row[field] if not pd.isna(row[field]) else None for field in row.index}
                
#                 # Skip the 'Unnamed: 0' column
#                 row_data = {field: row[field] for field in row.index if field != 'Unnamed: 0' and not pd.isna(row[field])}
                
#                 # Create and save the Household object
#                 household = Household(**row_data)
#                 household.save()

#             os.remove(file_path)  # Delete the file after processing
#             messages.success(request, "Dataset imported successfully.")
#         except Exception as e:
#             messages.error(request, f"Error during import: {e}")
#             if os.path.exists(file_path):
#                 os.remove(file_path)  # Make sure to delete the file in case of error

#         return redirect('home')

#     return redirect('home')


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

# Household Demographics Page
def household_demographics(request):
    household_instance = Household.objects.first()
    context = {'household': household_instance}
    return render(request, "pages/1 - household-demographics/household-demographics.html", context)

# Economic Wellbeing Page

def economic_wellbeing(request):
    context = {}

    # Query the database to get the count for each water quality option
    excellent_count = HouseholdProperty.objects.filter(water_quality=1).count()
    mostly_good_count = HouseholdProperty.objects.filter(water_quality=2).count()
    sometimes_good_count = HouseholdProperty.objects.filter(water_quality=3).count()
    poor_count = HouseholdProperty.objects.filter(water_quality=4).count()
    very_poor_count = HouseholdProperty.objects.filter(water_quality=5).count()
    empty_cells_count = HouseholdProperty.objects.filter(water_quality__isnull=True).count()

    # Calculate the total count
    total_count = excellent_count + mostly_good_count + sometimes_good_count + poor_count + very_poor_count + empty_cells_count

    # Calculate the percentage for each option
    excellent_percentage = (excellent_count / total_count) * 100 if total_count > 0 else 0
    mostly_good_percentage = (mostly_good_count / total_count) * 100 if total_count > 0 else 0
    sometimes_good_percentage = (sometimes_good_count / total_count) * 100 if total_count > 0 else 0
    poor_percentage = (poor_count / total_count) * 100 if total_count > 0 else 0
    very_poor_percentage = (very_poor_count / total_count) * 100 if total_count > 0 else 0
    empty_cells_percentage = (empty_cells_count / total_count) * 100 if total_count > 0 else 0

    # Calculate the overall score out of 10 including empty cells
    # overall_score = (excellent_count * 5 + mostly_good_count * 4 + sometimes_good_count * 3 + poor_count * 2 + very_poor_count * 1) / total_count if total_count > 0 else 0
    overall_score = (excellent_count * 5 + mostly_good_count * 4 + sometimes_good_count * 3 + poor_count * 2 + very_poor_count * 1) / (total_count - empty_cells_count) if total_count > 0 else 0


    # Pass the data to the template
    context['excellent_count'] = excellent_count
    context['mostly_good_count'] = mostly_good_count
    context['sometimes_good_count'] = sometimes_good_count
    context['poor_count'] = poor_count
    context['very_poor_count'] = very_poor_count
    context['empty_cells_count'] = empty_cells_count

    context['excellent_percentage'] = round(excellent_percentage, 2)
    context['mostly_good_percentage'] = round(mostly_good_percentage, 2)
    context['sometimes_good_percentage'] = round(sometimes_good_percentage, 2)
    context['poor_percentage'] = round(poor_percentage, 2)
    context['very_poor_percentage'] = round(very_poor_percentage, 2)
    context['empty_cells_percentage'] = round(empty_cells_percentage, 2)

    context['overall_score'] = round(overall_score, 2)
    
    # ###################################### ELECTRICITY DISRUPTION CALCULATION   ########################################################################
    
     # Query the database to get the count for each electricity disruption option
    never_count = HouseholdProperty.objects.filter(electricity_disruption=1).count()
    several_times_a_year_count = HouseholdProperty.objects.filter(electricity_disruption=2).count()
    once_a_month_count = HouseholdProperty.objects.filter(electricity_disruption=3).count()
    once_a_week_count = HouseholdProperty.objects.filter(electricity_disruption=4).count()
    several_times_a_week_count = HouseholdProperty.objects.filter(electricity_disruption=5).count()
    everyday_count = HouseholdProperty.objects.filter(electricity_disruption=6).count()
    no_power_supply_count = HouseholdProperty.objects.filter(electricity_disruption=7).count()

    # Calculate the total count
    total_count = never_count + several_times_a_year_count + once_a_month_count + once_a_week_count + several_times_a_week_count + everyday_count + no_power_supply_count

    # Calculate the percentage for each option
    never_percentage = (never_count / total_count) * 100 if total_count > 0 else 0
    several_times_a_year_percentage = (several_times_a_year_count / total_count) * 100 if total_count > 0 else 0
    once_a_month_percentage = (once_a_month_count / total_count) * 100 if total_count > 0 else 0
    once_a_week_percentage = (once_a_week_count / total_count) * 100 if total_count > 0 else 0
    several_times_a_week_percentage = (several_times_a_week_count / total_count) * 100 if total_count > 0 else 0
    everyday_percentage = (everyday_count / total_count) * 100 if total_count > 0 else 0
    no_power_supply_percentage = (no_power_supply_count / total_count) * 100 if total_count > 0 else 0

    # Pass the data to the template
    context['never_percentage'] = round(never_percentage, 2)
    context['several_times_a_year_percentage'] = round(several_times_a_year_percentage, 2)
    context['once_a_month_percentage'] = round(once_a_month_percentage, 2)
    context['once_a_week_percentage'] = round(once_a_week_percentage, 2)
    context['several_times_a_week_percentage'] = round(several_times_a_week_percentage, 2)
    context['everyday_percentage'] = round(everyday_percentage, 2)
    context['no_power_supply_percentage'] = round(no_power_supply_percentage, 2)
    
    ########################### HOUSING TYPE CALCULATION ###########################################################
    
    
    # Calculate the number of people with different housing types
    total_households = HouseholdProperty.objects.count()
    separate_apartment_count = HouseholdProperty.objects.filter(housing_type=1).count()
    separate_house_count = HouseholdProperty.objects.filter(housing_type=2).count()
    other_dwelling_count = HouseholdProperty.objects.filter(housing_type=3).count()

    # Calculate the number of empty cells
    empty_cells_count = HouseholdProperty.objects.filter(housing_type__isnull=True).count()

    # Calculate percentages
    separate_apartment_percentage = (separate_apartment_count / total_households) * 100
    separate_house_percentage = (separate_house_count / total_households) * 100
    other_dwelling_percentage = (other_dwelling_count / total_households) * 100
    empty_cells_percentage = (empty_cells_count / total_households) * 100

    context['total_households'] = total_households
    context['separate_apartment_count'] = separate_apartment_count
    context['separate_apartment_percentage'] = round(separate_apartment_percentage, 2)

    context['separate_house_count'] = separate_house_count
    context['separate_house_percentage'] = round(separate_house_percentage, 2)

    context['other_dwelling_count'] = other_dwelling_count
    context['other_dwelling_percentage'] = round(other_dwelling_percentage, 2)

    context['empty_cells_count'] = empty_cells_count
    context['empty_cells_percentage'] = round(empty_cells_percentage, 2)

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