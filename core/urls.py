from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from core import views


urlpatterns = [
    path("", views.index, name="home"),
]

# Map MEDIA_URL with MEDIA_ROOT on local developments
APP_ENVIRONMENT = getattr(settings, "APP_ENVIRONMENT", "local")

if APP_ENVIRONMENT == "local":
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
