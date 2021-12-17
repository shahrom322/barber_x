from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='home'),

    path('about/', views.AboutView.as_view(), name='about'),

    path('service/', views.ServiceView.as_view(), name='service'),
    path('service/<str:url>', views.PriceByService.as_view(), name='single_service'),

    path('price/', views.PriceView.as_view(), name='price'),

    path('team/', views.TeamView.as_view(), name='team'),

    path('gallery/', views.GalleryView.as_view(), name='gallery'),

    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<slug:id>/', views.SinglePageView.as_view(), name='single_page'),

    path('contact/', views.ContactView.as_view(), name='contact'),

    path('newsletter/', views.NewsLetterView.as_view(), name='newsletter'),
]