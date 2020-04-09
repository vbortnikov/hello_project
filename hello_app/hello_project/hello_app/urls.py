from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('metrics/', views.metrics, name='prometheus'),
    path('health/', views.healthCheck, name='health'),
    path('ready/', views.readyCheck, name='ready'),
]