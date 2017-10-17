"""django_mobile_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from django.core.urlresolvers import reverse_lazy
# from django.views.generic.base import RedirectView
from .views import (
    about, services, contact, Home
)


urlpatterns = [
    # Redirect home to admin-home
    # url(r'^$', RedirectView.as_view(
    #     url=reverse_lazy('admin:index'),
    #     permanent=False)
    #     ),
    # url(r'^$', home, name='home'),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^about/', about, name='about'),
    url(r'^services/', services, name='services'),
    url(r'^contact/', contact, name='contact'),
    url(r'^chaining/', include('smart_selects.urls')),  # Django smart-selects
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
