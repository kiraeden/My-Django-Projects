from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('', views.RegistrationView.as_view(), name='create_account'),
    path('register/', views.register, name='register'),
]