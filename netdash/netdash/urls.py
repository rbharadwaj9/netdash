"""NetDash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from .views import login, logout


urlpatterns = [
    path('', include('netdash_ui.urls')),
    path('api/', include('netdash_api.urls')),
    path('admin/', admin.site.urls),
    path('account/login', login, name='login'),
    path('account/logout', logout, name='logout'),
]

if hasattr(settings, 'SAML_CONFIG'):
    from djangosaml2 import views as saml_views
    urlpatterns += (path('saml/', include('djangosaml2.urls')),)
    if settings.DEBUG:
        urlpatterns += (path('saml/test/', saml_views.echo_attributes, name='saml2_test'),)
