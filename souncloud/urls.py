from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from download.views import home , download

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('download/', download, name='download'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)