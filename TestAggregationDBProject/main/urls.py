from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ReleaseView.as_view(), name='release'),
    path('<str:name>/<int:pk>/', views.ModelsView.as_view(), name='models'),
    path('<str:name>/<str:version>/<int:pk>/', views.DataView.as_view(), name='data')
]