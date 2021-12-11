from django.urls import path
from . import views


urlpatterns = [
    path('', views.test, name='home'),

    path('about/', views.about, name='about'),

    path('service/', views.service, name='service'),
    path('service/<int:id>', views.service, name='single_service'),

    path('price/', views.price, name='price'),

    path('team/', views.team, name='team'),
    # TODO делать страницу с профилем барбера?

    path('gallery/', views.gallery, name='gallery'),

    path('blog/', views.blog, name='blog'),
    path('blog/<str:slug>', views.single_page, name='single_page'),

    path('contact/', views.contact, name='contact'),
]