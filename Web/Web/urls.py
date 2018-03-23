"""Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.general.views import index, index1, index2, index3, index4, nosotros_view, productos_view, servicios_view,contactanos_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name = 'index'),
    url(r'^1/$', index1, name = 'index1'),
    url(r'^2/$', index2, name = 'index2'),
    url(r'^3/$', index3, name = 'index3'),
    url(r'^4/$', index4, name = 'index4'),
    url(r'^nosotros/$', nosotros_view, name = 'nosotros'),
    url(r'^productos/$', productos_view, name = 'productos'),
    url(r'^servicios/$', servicios_view, name = 'servicios'),
    url(r'^contactanos/$', contactanos_view, name = 'contactanos'),
]
