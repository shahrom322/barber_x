from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView

from barber.forms import ApplicationForm
from barber.models import Barber, Service, Product, Post


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


def team(request):
    return render(request, 'barber/team.html')


def gallery(request):
    return render(request, 'barber/gallery.html')

class BlogView(TemplateView):
    def get(self, request):
        return render(request, 'barber/blog.html', {'posts': Post.objects.all()})


class SinglePageView(DetailView):
    model = Post
    template_name = 'barber/single_page.html'
    slug_url_kwarg = 'id'
    context_object_name = 'post'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)


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
