from django.contrib import admin
from .models import Service, Product, Barber, Application, Post, PortfolioImage

admin.site.register(Service)
admin.site.register(Product)
admin.site.register(Barber)
admin.site.register(Application)
admin.site.register(Post)
admin.site.register(PortfolioImage)