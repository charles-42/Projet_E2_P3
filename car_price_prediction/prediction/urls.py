# prediction/urls.py
from django.urls import path
from . import views

app_name = 'prediction'

urlpatterns = [
    path('', views.predict_car_price, name='predict'),
]