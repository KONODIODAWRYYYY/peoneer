from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views

urlpatterns = format_suffix_patterns([
    path('about', views.IntroViewSet.as_view({'get' : 'retrieve'})),
    path('', views.IntroViewSet.as_view({'get' : 'list'})),
])