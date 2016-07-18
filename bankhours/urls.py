"""bankhours URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
# Import URLS
from bankhours.core import urls as core_urls 
from bankhours.accounts import urls as accounts_urls
from bankhours.bank_of_hours import urls as bank_of_hours_urls 
from bankhours.employee import urls as employee_urls 

urlpatterns = [
    url(r'^', include(core_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^', include(bank_of_hours_urls)),
    url(r'^', include(employee_urls)),
    url(r'^admin/', admin.site.urls),
]


