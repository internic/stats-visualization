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