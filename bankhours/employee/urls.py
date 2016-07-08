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
    url(r'^employee/add/$', EmployeeCreate.as_view(), name='employee_add'),
    url(r'^employee/details/(?P<pk>[0-9]+)/$', EmployeeDetails.as_view(), name='employee_details'),
    url(r'^employee/edit/(?P<pk>[0-9]+)/$', EmployeeUpdate.as_view(), name='employee_edit'),
    url(r'^employee/(?P<pk>[0-9]+)/delete/$', EmployeeDelete.as_view(), name='employee_delete'),
    # BankOfHours
    url(r'^bank-of-hours/list/$', BankOfHoursList.as_view(), name='bank_of_hours_list'),
    url(r'^bank-of-hours/add/$', BankOfHoursCreate.as_view(), name='bank_of_hours_add'),
    url(r'^bank-of-hours/details/(?P<pk>[0-9]+)/$', BankOfHoursDetails.as_view(), name='bank_of_hours_details'),
    url(r'^bank-of-hours/edit/(?P<pk>[0-9]+)/$', BankOfHoursUpdate.as_view(), name='bank_of_hours_edit'),
    url(r'^bank-of-hours/(?P<pk>[0-9]+)/delete/$', BankOfHoursDelete.as_view(), name='bank_of_hours_delete'),
    # Compensation
    url(r'^compensation/list/$', CompensationList.as_view(), name='compensation_list'),
    url(r'^compensation/add/$', CompensationCreate.as_view(), name='compensation_add'),
    url(r'^compensation/details/(?P<pk>[0-9]+)/$', CompensationDetails.as_view(), name='compensation_details'),
    url(r'^compensation/edit/(?P<pk>[0-9]+)/$', CompensationUpdate.as_view(), name='compensation_edit'),
    url(r'^compensation/(?P<pk>[0-9]+)/delete/$', CompensationDelete.as_view(), name='compensation_delete'),
]
