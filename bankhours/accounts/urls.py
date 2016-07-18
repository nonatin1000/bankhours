from django.conf.urls import url
from django.contrib.auth import views
from django.contrib.auth import urls
from .views import edit
from .forms import PasswordResetForm, EditAccountForm

urlpatterns = [
	# Edit User
	url(r'^user/edit/$', edit, name='edit'),
    # Login
    url(r'^login/$', views.login, {'template_name': 'accounts/login.html'}, name='login'), 
    url(r'^logout/$', views.logout_then_login, {'login_url': 'index'}, name='logout'),
    # Recovery Password
	url(r'^password_change/$', views.password_change, { 'template_name': 'accounts/password_change.html'}, name='password_change'),
	url(r'^password_change/done/$', views.password_change_done, { 'template_name': 'accounts/password_change_done.html'}, name='password_change_done'),
	url(r'^password_reset/$', views.password_reset, { 'from_email': 'Não Responder <naoresponder@saudecoletivapicos.com.br>',  
		'template_name': 'accounts/password_reset.html', 'html_email_template_name': 'accounts/password_reset_email.html', 'password_reset_form':PasswordResetForm}, name='password_reset'),
	url(r'^password_reset/done/$', views.password_reset_done, { 'template_name': 'accounts/password_reset_done.html'}, name='password_reset_done'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		views.password_reset_confirm, { 'template_name': 'accounts/password_reset_confirm.html'}, name='password_reset_confirm'),
	url(r'^reset/done/$', views.password_reset_complete, { 'template_name': 'accounts/password_reset_complete.html'}, name='password_reset_complete'),
]