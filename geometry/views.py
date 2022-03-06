from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def rectangle_area(request, width: int, height: int):
    answer = (width * height)
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {answer}')


def square_area(request, width: int):
    answer = (width ** 2)
    return HttpResponse(f'Площадь квадрата со стороной {width} равна {answer}')


def circle_area(request, radius: int):
    from math import pi
    answer = round((pi * radius ** 2), 2)
    return HttpResponse(f'Площадь круа с радиусом {radius} равна {answer}')


def get_rectangle_area(request, width: int, height: int):
    rectangle_redirect = reverse('rectangle', args=[width, height])
    return HttpResponseRedirect(rectangle_redirect)


def get_square_area(request, width: int):
    square_redirect = reverse('square', args=[width])
    return HttpResponseRedirect(square_redirect)


def get_circle_area(request, radius: int):
    circle_redirect = reverse('circle', args=[radius])
    return HttpResponseRedirect(circle_redirect)
