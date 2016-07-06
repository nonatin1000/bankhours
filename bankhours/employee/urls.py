from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^list/$', FunctionList.as_view(), name='function_list'),
    url(r'^add/$', FunctionCreate.as_view(), name='function_add'),
	url(r'^details/(?P<pk>[0-9]+)/$', FunctionDetail.as_view(), name='function_details'),
	url(r'^edit/(?P<pk>[0-9]+)/$', FunctionUpdate.as_view(), name='function_update'),
	url(r'^(?P<pk>[0-9]+)/delete/$', FunctionDelete.as_view(), name='function_delete'),
]
