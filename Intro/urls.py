from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views

urlpatterns = format_suffix_patterns([
    path('', views.default_intro),
])