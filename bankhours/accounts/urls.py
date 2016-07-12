from django.conf.urls import url
from django.contrib.auth.views import logout_then_login, login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
#from .views import *

urlpatterns = [
    # Login
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'), 
    url(r'^logout/$', logout_then_login, {'login_url': 'core:home'}, name='logout'),
]
