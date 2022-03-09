from django.urls import path, register_converter
from . import views as views, converters

register_converter(converters.FourDigitConverter, 'yyyy')
register_converter(converters.FloatDigitConverter, 'float')
register_converter(converters.DateConverter, 'date')

urlpatterns = [
    path('', views.index, name='horoscope_index'),
    path('kiany', views.get_kiany_info),
    path('guinnessworldrecords', views.get_guinness_world_records),
    path('<date:number>', views.get_date_converters),
    path('type', views.show_types),
    path('type/<str:element>', views.show_element_signs, name='type_name'),
    path('<int:month>/<int:day>', views.day_month),
    path('<yyyy:number>', views.get_yyyy_converters),
    path('<int:sign_zodiac>', views.get_info_about_zodiac_sign_by_number),
    path('<float:number>', views.get_float_converters),
    path('<str:sign_zodiac>', views.get_info_about_zodiac_sign, name='horoscope_name'),
]
