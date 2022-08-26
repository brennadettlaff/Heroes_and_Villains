from django.urls import path
from . import views

urlspatterns = [
    path('', views.supers_list),
    path('<int:pk>/', views.supers_detail)
]