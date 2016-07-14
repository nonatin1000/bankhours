from django.conf.urls import url
from .views import *

urlpatterns = [
    # Function
	url(r'^function/list/$', FunctionList.as_view(), name='function_list'),
    url(r'^function/add/$', FunctionCreate.as_view(), name='function_add'),
	url(r'^function/details/(?P<pk>[0-9]+)/$', FunctionDetail.as_view(), name='function_details'),
	url(r'^function/edit/(?P<pk>[0-9]+)/$', FunctionUpdate.as_view(), name='function_edit'),
	url(r'^function/(?P<pk>[0-9]+)/delete/$', FunctionDelete.as_view(), name='function_delete'),
    # Department
    url(r'^department/list/$', DepartmentList.as_view(), name='department_list'),
    url(r'^department/add/$', DepartmentCreate.as_view(), name='department_add'),
    url(r'^department/details/(?P<pk>[0-9]+)/$', DepartmentDetail.as_view(), name='department_details'),
    url(r'^department/edit/(?P<pk>[0-9]+)/$', DepartmentUpdate.as_view(), name='department_edit'),
    url(r'^department/(?P<pk>[0-9]+)/delete/$', DepartmentDelete.as_view(), name='department_delete'),
    # Employee
    url(r'^employee/list/$', EmployeeList.as_view(), name='employee_list'),
    url(r'^employee-autocomplete/$', EmployeeAutocomplete.as_view(), name='employee_autocomplete'), 
    url(r'^employee/add/$', EmployeeCreate.as_view(), name='employee_add'),
    url(r'^employee/details/(?P<pk>[0-9]+)/$', EmployeeDetails.as_view(), name='employee_details'),
    url(r'^employee/edit/(?P<pk>[0-9]+)/$', EmployeeUpdate.as_view(), name='employee_edit'),
    url(r'^employee/(?P<pk>[0-9]+)/delete/$', EmployeeDelete.as_view(), name='employee_delete'),
    url(r'^employee/report-employee-period/(?P<pk>[0-9]+)/$', HoursReportByTheOfficialPeriod.as_view(), name='hours_report_by_the_official_period'),
]
