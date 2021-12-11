from django.urls import path
from . import views


urlpatterns = [
    path('', views.test, name='home'),

    path('about/', views.AboutView.as_view(), name='about'),

    path('service/', views.ServiceView.as_view(), name='service'),
    path('service/<str:url>', views.ServiceView.as_view(), name='single_service'),

    path('price/', views.PriceView.as_view(), name='price'),

    path('team/', views.team, name='team'),
    # TODO делать страницу с профилем барбера?

    path('gallery/', views.gallery, name='gallery'),

    path('blog/', views.blog, name='blog'),
    path('blog/<str:slug>', views.single_page, name='single_page'),

    path('contact/', views.contact, name='contact'),
]