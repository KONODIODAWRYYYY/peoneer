from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'TimeTable'
urlpatterns = format_suffix_patterns([
	path('', views.table, name = 'table'),
	path('<int:course>', views.table, name = 'course'),
])