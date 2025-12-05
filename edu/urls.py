from django.urls import path
from .views import home_page,filter_markazlar, batafsil_malumot

urlpatterns = [
    path('', home_page, name='home'),
    path('filter/<int:kat_id>/', filter_markazlar, name='filter'), 
    path('markaz/<int:pk>/', batafsil_malumot, name='detail'), 
]