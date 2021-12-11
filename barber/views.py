from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from barber.models import Barber, Service


def test(request):
    return render(request, 'barber/index.html')


class AboutView(TemplateView):

    def get(self, request):
        barbers = Barber.objects.all()
        return render(
            self.request,
            'barber/about.html',
            {
                'barbers': barbers
            }
        )


class ServiceView(TemplateView):

    def get(self, request):
        services = Service.objects.all()
        return render(
            request,
            'barber/service.html',
            {
                'services': services
            }
        )


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