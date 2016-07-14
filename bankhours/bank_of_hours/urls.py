from django.conf.urls import url
from .views import *

urlpatterns = [
    # Autocomplete
    url(r'^bank-of-hours-autocomplete/$', BankOfHoursAutocomplete.as_view(), name='bank_of_hours_autocomplete'), 
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
    # Report
    url(r'^employee/report-all-employee-period/$', ReportAllEmployeePeriod.as_view(), name='report_all_employee_period'),
]
