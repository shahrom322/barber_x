import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('barber.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
