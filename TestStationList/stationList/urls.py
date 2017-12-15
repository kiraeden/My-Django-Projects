from django.urls import path
from . import views

app_name = "stationList"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('editStation/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('addStation/', views.AddView.as_view(), name='add'),
]