from django.contrib import admin
from .models import Household, Individual, Education, ChildHealth, ChildHealthDetails, HouseholdProperty, HouseholdAsset, HouseholdFinance, HouseholdFoodConsumption, HouseholdNonFoodExpenditure, HouseholdIncome, HouseholdTransfer, HouseholdShock, HouseholdClimateChangeResponse

admin.site.register(Household)
admin.site.register(Individual)
admin.site.register(Education)
admin.site.register(ChildHealth)
admin.site.register(ChildHealthDetails)
admin.site.register(HouseholdProperty)
admin.site.register(HouseholdAsset)
admin.site.register(HouseholdFinance)
admin.site.register(HouseholdFoodConsumption)
admin.site.register(HouseholdNonFoodExpenditure)
admin.site.register(HouseholdIncome)
admin.site.register(HouseholdTransfer)
admin.site.register(HouseholdShock)
admin.site.register(HouseholdClimateChangeResponse)

