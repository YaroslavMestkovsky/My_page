from django.urls import path
from . import views as views

urlpatterns = [
    path('', views.index),
    path('type', views.show_types),
    path('type/<str:element>', views.show_element_signs, name='type_name'),
    path('<int:month>/<int:day>', views.day_month),
    path('<int:sign_zodiac>', views.get_info_about_zodiac_sign_by_number),
    path('<str:sign_zodiac>', views.get_info_about_zodiac_sign, name='horoscope_name'),
]
