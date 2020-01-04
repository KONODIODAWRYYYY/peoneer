from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns ([
    path("", views.RoomAPIView.as_view({'get':"list"})),
    path("floors/<int:floor>", views.RoomAPIView.as_view({'get':"list"})),
    path("rooms/<str:pk>", views.RoomAPIView.as_view({'get':"retrieve"})),
]
)
