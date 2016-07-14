from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from dal import autocomplete
from django.db.models import Q,Sum
from django.db.models.functions import Coalesce

from .models import *
from .forms import *

# Autocomplete BankOfHours
class BankOfHoursAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !
		
		qs = BankOfHours.objects.all()

		if self.q:
			qs = qs.filter(employee__name__istartswith=self.q)

		return qs

class BankOfHoursList(ListView):

	model = BankOfHours
	template_name = 'bankofhours/list.html'

class BankOfHoursCreate(CreateView):

	model = BankOfHours
	template_name = 'bankofhours/add.html'
	form_class = BankOfHoursForm

class BankOfHoursUpdate(UpdateView):

	model = BankOfHours
	template_name = 'bankofhours/add.html'
	form_class = BankOfHoursForm

class BankOfHoursDetails(DetailView):

	model = BankOfHours
	template_name = 'bankofhours/details.html'

class BankOfHoursDelete(DeleteView):

	model = BankOfHours
	success_url = reverse_lazy('bank_of_hours:bank_of_hours_list')
	template_name = 'bankofhours/delete.html'

class CompensationList(ListView):

	model = Compensation
	template_name = 'compensation/list.html'

class CompensationCreate(CreateView):

	model = Compensation
	template_name = 'compensation/add.html'
	form_class = CompensationForm

class CompensationUpdate(UpdateView):

	model = Compensation
	template_name = 'compensation/add.html'
	form_class = CompensationForm

class CompensationDetails(DetailView):

	model = Compensation
	template_name = 'compensation/details.html'

class CompensationDelete(DeleteView):

	model = Compensation
	success_url = reverse_lazy('bank_of_hours:compensation_list')
	template_name = 'compensation/delete.html'

class ReportEmployeePeriod(ListView):

	model = BankOfHours
	template_name = 'reports/employee_period.html'

	def get_queryset(self):
		self.queryset = super(ReportEmployeePeriod,self).get_queryset()
		self.filtro_form=FilterForm(self.request.GET)
		self.filtro_form.is_valid()
		if self.request.GET.get('pesquisa', False) :
			self.queryset=self.queryset.filter(Q(employee__name__icontains = self.request.GET['pesquisa']))
		if self.filtro_form.cleaned_data.get('de', False) :
			self.queryset=self.queryset.filter(work_date__gte = self.filtro_form.cleaned_data['de'])
		if self.filtro_form.cleaned_data.get('ate', False) :
			self.queryset=self.queryset.filter(work_date__lte = self.filtro_form.cleaned_data['ate'])
		self.queryset.order_by("work_date")
		return self.queryset