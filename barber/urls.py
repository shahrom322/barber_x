from django.urls import path
from . import views


urlpatterns = [
    path('', views.test, name='home'),

    path('about/', views.AboutView.as_view(), name='about'),

    path('service/', views.ServiceView.as_view(), name='service'),
    path('service/<str:url>', views.PriceByService.as_view(), name='single_service'),

    path('price/', views.PriceView.as_view(), name='price'),

    path('team/', views.TeamView.as_view(), name='team'),
    # TODO делать страницу с профилем барбера?

    path('gallery/', views.GalleryView.as_view(), name='gallery'),

    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>', views.SinglePageView.as_view(), name='single_page'),

    path('contact/', views.ContactView.as_view(), name='contact'),
]