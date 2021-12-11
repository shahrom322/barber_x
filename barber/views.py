from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from barber.models import Barber, Service, Product


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


class PriceByService(TemplateView):

    def get(self, request, url):
        service = get_object_or_404(Service, url=url)
        products = Product.objects.all() # TODO filter(service=service)
        return render(
            request,
            'barber/service.html',
            {
                'service': service,
                'products': products
            }
        )


class PriceView(TemplateView):

    def price(self, request):
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