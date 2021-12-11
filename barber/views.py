from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    return render(request, 'barber/index.html')


def about(request):
    return render(request, 'barber/about.html')


def service(request):
    return render(request, 'barber/service.html')


def price(request):
    return render(request, 'barber/price.html')


def team(request):
    return render(request, 'barber/team.html')


def gallery(request):
    return render(request, 'barber/gallery.html')


def blog(request):
    return render(request, 'barber/blog.html')


def single_page(request):
    return render(request, 'barber/single_page.html')


def contact(request):
    return render(request, 'barber/contact.html')
