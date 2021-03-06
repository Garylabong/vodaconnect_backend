"""GPGVODAConnectApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings

from authentication.views import ClientViewSet
from django.views.generic import TemplateView

from rest_framework import authentication, routers

router = routers.DefaultRouter()
router.register(r"clients", ClientViewSet)

urlpatterns = [
    # path("", TemplateView.as_view(template_name="index.html")),
    path("billing/", include("Billing.urls")),
    path("auth/", include("authentication.urls")),
    path("", include("SubscribersInventory.urls")),
    path("order/", include("OrderRequest.urls")),
    path("account/files/", include("AccountFiles.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("api/", include(router.urls)),
    # for vues connection
    path("api/v1", include("djoser.urls")),
    path("api/v1", include("djoser.urls.authtoken")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
