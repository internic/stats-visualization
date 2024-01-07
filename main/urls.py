from django.urls import path
from . import views
from .views import HouseholdDemographicsView

urlpatterns = [
    # path("", views.home, name="home"),
    # path("dashboard/", views.dashboard, name="dashboard"),
    path("", HouseholdDemographicsView.as_view(), name='household-demographics'),
    path('import_dataset/', views.import_dataset, name='import_dataset'),
    path('economic-wellbeing/', views.economic_wellbeing, name='economic-wellbeing'),
    path('housing-amenities/', views.housing_and_amenities, name='housing-and-amenities'),
    path('education-employment/', views.education_and_employment, name='education-employment'),
    path('health-nutrition/', views.health_and_nutrition, name='health-nutrition'),
    path('migration-remittances/', views.migration_and_remittances, name='migration-remittances'),
    path('family-background/', views.shocks_and_coping_mechanism, name='family-background'),
    path('community-perception/', views.community_perception, name='community-perception'),

]