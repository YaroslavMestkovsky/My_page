from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def rectangle_area(request):
    return render(request, 'geometry/rectangle.html')


def square_area(request):
    return render(request, 'geometry/square.html')


def circle_area(request):
    return render(request, 'geometry/circle.html')


def get_rectangle_area(request, width: int, height: int):
    rectangle_redirect = reverse('rectangle', args=[width, height])
    return HttpResponseRedirect(rectangle_redirect)


def get_square_area(request, width: int):
    square_redirect = reverse('square', args=[width])
    return HttpResponseRedirect(square_redirect)


def get_circle_area(request, radius: int):
    circle_redirect = reverse('circle', args=[radius])
    return HttpResponseRedirect(circle_redirect)
