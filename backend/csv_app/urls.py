from django.urls import path
from .views import CSV_File

app_name = 'csv_app'

urlpatterns = [
    path('', CSV_File.as_view(), name='csv'),
]
