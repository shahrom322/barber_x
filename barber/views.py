from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from barber.forms import ApplicationForm
from barber.models import Barber, Service, Product, Post, PortfolioImage


class MainView(TemplateView):

    def get(self, request):

        return render(
            request,
            'barber/index.html',
            {
                'services': Service.objects.all(),
                'barbers': Barber.objects.all().select_related(),
                'products': Product.objects.all(),
                'posts': Post.objects.all(),
                'form': ApplicationForm()
            }
        )

    def post(self, request):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(
            request,
            'barber/contact.html',
            {
                'form': form
            }
        )


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
        products = Product.objects.filter(service=service)
        return render(
            request,
            'barber/price.html',
            {
                'service': service,
                'products': products
            }
        )


class PriceView(TemplateView):

    def get(self, request):
        return render(
            request,
            'barber/price.html',
            {
                'products': Product.objects.all()
            }
        )


class TeamView(TemplateView):

    def get(self, request):
        return render(
            request,
            'barber/team.html',
            {'barbers': Barber.objects.all()}
        )


class GalleryView(TemplateView):

    def get(self, request):
        query = request.GET.get('q')
        services = Service.objects.all()
        if query:
            portfolio_images = PortfolioImage.objects.filter(service__url=query)
            print(portfolio_images)
        else:
            portfolio_images = PortfolioImage.objects.all()

        return render(
            request, 'barber/gallery.html',
            {
                'portfolio_images': portfolio_images,
                'services': services
            }
        )


def blog(request):
    return render(request, 'barber/blog.html')


class SinglePageView(TemplateView):

    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        return render(
            request,
            'barber/single_page.html',
            {
                'post': post
            }
        )


class ContactView(TemplateView):

    def get(self, request):
        form = ApplicationForm()
        return render(
            request,
            'barber/contact.html',
            {
                'form': form
            }
        )

    def post(self, request):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(
            request,
            'barber/contact.html',
            {
                'form': form
            }
        )

def p(self):
    pass