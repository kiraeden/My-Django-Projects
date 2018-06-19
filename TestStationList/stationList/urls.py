from django.urls import path
from . import views

app_name = "stationList"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('editStation/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('addStation/', views.AddView.as_view(), name='add'),
    path('checkout/', views.check_out_station, name='checkout'),
    path('release/', views.release_station, name='release'),
    path('add_new/', views.add_station, name='add_station'),    
    path('apply_edits/', views.edit_station, name='edit_station'),
    path('delete_station/', views.delete_station, name='delete_station'),
    path('update_maintenance/', views.update_maintenance, name='update_maintenance')
]