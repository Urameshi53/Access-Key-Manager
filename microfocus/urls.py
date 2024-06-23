"""
URL configuration for microfocus project.

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework import routers

from tenant import views
from tenant.views import IndexView

router = routers.DefaultRouter()
router.register(r'schools', views.SchoolViewSet)
router.register(r'keys', views.KeyViewSet)

urlpatterns = [
    path('admin/', admin.site.index , name='admin'),
    path('', IndexView.as_view(), name='home'),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('tenant/', include('tenant.urls')),
    path('accounts/', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
