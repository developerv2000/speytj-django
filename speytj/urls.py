"""
URL configuration for speytj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("", include("core.urls")),
    path("admin/", admin.site.urls),
]


# Add django-debug-toolbar’s URLs
if settings.ENABLE_DJANGO_DEBUG_TOOLBAR and not settings.TESTING:
    urlpatterns += debug_toolbar_urls()


# Map MEDIA_URL with MEDIA_ROOT on local developments
APP_ENVIRONMENT = getattr(settings, "APP_ENVIRONMENT", "local")

if APP_ENVIRONMENT == "local":
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
