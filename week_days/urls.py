from django.urls import path
from . import views as views

urlpatterns = [
    path('', views.index),
    path('<int:day>', views.get_info_about_day_by_number),
    path('<str:day>', views.get_info_about_day, name='day_name'),
]
