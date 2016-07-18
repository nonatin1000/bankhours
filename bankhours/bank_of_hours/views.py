from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from dal import autocomplete
from django.db.models import Sum
from django.db.models.functions import Coalesce

from .models import *
from .forms import *
from bankhours.employee.models import Employee

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Autocomplete BankOfHours
@method_decorator(login_required, name='dispatch')
class BankOfHoursAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !
		
		qs = BankOfHours.objects.all()

		if self.q:
			qs = qs.filter(employee__name__istartswith=self.q)

		return qs

@method_decorator(login_required, name='dispatch')
class BankOfHoursList(ListView):

	paginate_by = 50

	model = BankOfHours
	template_name = 'bankofhours/list.html'

	def get_queryset(self):
		self.queryset = super(BankOfHoursList,self).get_queryset()
		if self.request.GET.get('search_box', False) :
			self.queryset=self.queryset.filter(employee__name__icontains = self.request.GET['search_box'])
		return self.queryset

@method_decorator(login_required, name='dispatch')
class BankOfHoursCreate(CreateView):

	model = BankOfHours
	template_name = 'bankofhours/add.html'
	form_class = BankOfHoursForm

@method_decorator(login_required, name='dispatch')
class BankOfHoursUpdate(UpdateView):

	model = BankOfHours
	template_name = 'bankofhours/add.html'
	form_class = BankOfHoursForm

@method_decorator(login_required, name='dispatch')
class BankOfHoursDetails(DetailView):

	model = BankOfHours
	template_name = 'bankofhours/details.html'

@method_decorator(login_required, name='dispatch')
class BankOfHoursDelete(DeleteView):

	model = BankOfHours
	success_url = reverse_lazy('bank_of_hours_list')
	template_name = 'bankofhours/delete.html'

@method_decorator(login_required, name='dispatch')
class CompensationList(ListView):

	paginate_by = 50

	model = Compensation
	template_name = 'compensation/list.html'

	def get_queryset(self):
		self.queryset = super(CompensationList,self).get_queryset()
		if self.request.GET.get('search_box', False) :
			self.queryset=self.queryset.filter(employee__name__icontains = self.request.GET['search_box'])
		return self.queryset

@method_decorator(login_required, name='dispatch')
class CompensationCreate(CreateView):

	model = Compensation
	template_name = 'compensation/add.html'
	form_class = CompensationForm

@method_decorator(login_required, name='dispatch')
class CompensationUpdate(UpdateView):

	model = Compensation
	template_name = 'compensation/add.html'
	form_class = CompensationForm

@method_decorator(login_required, name='dispatch')
class CompensationDetails(DetailView):

	model = Compensation
	template_name = 'compensation/details.html'

@method_decorator(login_required, name='dispatch')
class CompensationDelete(DeleteView):

	model = Compensation
	success_url = reverse_lazy('compensation_list')
	template_name = 'compensation/delete.html'

@method_decorator(login_required, name='dispatch')
class ReportAllEmployeePeriod(ListView):

	model = BankOfHours
	template_name = 'reports/report_all_employee_period.html'

	def get_queryset(self):
		self.queryset = super(ReportAllEmployeePeriod,self).get_queryset()
		self.filtro_form=FilterForm(self.request.GET)
		self.filtro_form.is_valid()
		return self.queryset

	def get_context_data(self, **kwargs):
		context = super(ReportAllEmployeePeriod,self).get_context_data(**kwargs)
		context['filtro_form']=self.filtro_form
		
		# Dicionario
		# Relatorio para exibir o nome do funcionario a quantidade horas extras, a quantidade de horas Compensadas e o saldo
		employees = Employee.objects.all()
		for employee in employees:
			bank_of_hours = employee.bank_of_hours.all()
			compensations = employee.compensations.all()
			
			if(self.filtro_form.cleaned_data.get('de', False)):
				compensations = compensations.filter(compensated_date__gte=self.filtro_form.cleaned_data['de'])
				bank_of_hours = bank_of_hours.filter(work_date__gte=self.filtro_form.cleaned_data['de'])
			if(self.filtro_form.cleaned_data.get('ate', False)):
				compensations=compensations.filter(compensated_date__lte=self.filtro_form.cleaned_data['ate'])
				bank_of_hours=bank_of_hours.filter(work_date__lte=self.filtro_form.cleaned_data['ate'])

			cumulative_hours = bank_of_hours.aggregate(total=Coalesce(Sum('cumulative_hours'),0))['total']
			amount_of_hours = compensations.aggregate(total=Coalesce(Sum('amount_of_hours'),0))['total']
			balance = cumulative_hours - amount_of_hours

			employee.cumulative_hours = cumulative_hours
			employee.amount_of_hours= amount_of_hours
			employee.balance = balance

		context['employees'] = employees

		return context