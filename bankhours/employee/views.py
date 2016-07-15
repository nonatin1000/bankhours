# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
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

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class FunctionList(ListView):
	
	model = Function
	template_name = 'function/list.html'

@method_decorator(login_required, name='dispatch')
class FunctionCreate(CreateView):

	model = Function 
	template_name = 'function/add.html'
	form_class = FunctionForm

@method_decorator(login_required, name='dispatch')
class FunctionUpdate(UpdateView):

	model = Function
	template_name = 'function/add.html'
	form_class = FunctionForm

@method_decorator(login_required, name='dispatch')
class FunctionDetail(DetailView):

	model = Function
	template_name = 'function/details.html'

@method_decorator(login_required, name='dispatch')
class FunctionDelete(DeleteView):

	model = Function
	success_url = reverse_lazy('employee:function_list')
	template_name = 'function/delete.html'

@method_decorator(login_required, name='dispatch')
class DepartmentList(ListView):

	model = Department
	template_name = 'department/list.html'

@method_decorator(login_required, name='dispatch')
class DepartmentCreate(CreateView):

	model = Department
	template_name = 'department/add.html'
	form_class = DepartmentForm

@method_decorator(login_required, name='dispatch')
class DepartmentUpdate(UpdateView):

	model = Department
	template_name = 'department/add.html'
	form_class = DepartmentForm

@method_decorator(login_required, name='dispatch')
class DepartmentDetail(DetailView):

	model = Department
	template_name = 'department/details.html'

@method_decorator(login_required, name='dispatch')
class DepartmentDelete(DeleteView):

	model = Department
	success_url = reverse_lazy('employee:department_list')
	template_name = 'department/delete.html'

@method_decorator(login_required, name='dispatch')
class EmployeeList(ListView):

	paginate_by = 50

	model = Employee
	template_name = 'employee/list.html'

	def get_queryset(self):
		self.queryset = super(EmployeeList,self).get_queryset()
		if self.request.GET.get('search_box', False) :
			self.queryset=self.queryset.filter(name__icontains = self.request.GET['search_box'])
		return self.queryset

# Autocomplete employee
@method_decorator(login_required, name='dispatch')
class EmployeeAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !
		
		qs = Employee.objects.all()

		if self.q:
			qs = qs.filter(name__istartswith=self.q)

		return qs

@method_decorator(login_required, name='dispatch')
class EmployeeCreate(CreateView):

	model = Employee
	template_name = 'employee/add.html'	
	form_class = EmployeeForm
	second_form_class = AddressForm

	def get(self, request, *args, **kwargs):
		self.object = None
		form = self.form_class
		address_form = self.second_form_class
		return self.render_to_response(
			self.get_context_data(
				form=form, 
				address_form=address_form
			)
		)

	def post(self, request, *args, **kwargs):
		self.object = None
		address_form = self.second_form_class(self.request.POST)
		form = self.form_class(self.request.POST)
		
		if form.is_valid() and address_form.is_valid():
			return self.form_valid(form, address_form)
		else:
			return self.form_invalid(form, address_form)

	def form_valid(self, form, address_form):
		self.object = address_form.save()
		employee = form.save(commit=False)
		employee.address = self.object
		employee.save()
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form, address_form):
		return self.render_to_response(
			self.get_context_data(	
					form=form,
                    address_form=address_form
			)
		)

	def get_success_url(self):
		return reverse('employee:employee_list')

@method_decorator(login_required, name='dispatch')
class EmployeeUpdate(UpdateView):

	model = Employee
	template_name = 'employee/add.html'	
	form_class = EmployeeForm
	second_form_class = AddressForm

	def get_context_data(self, **kwargs):
		self.object = self.get_object()
		context = super(EmployeeUpdate, self).get_context_data(**kwargs)
		if self.request.POST:
			context['address_form'] = self.second_form_class(self.request.POST, instance=self.object)
			context['form'] = self.form_class(self.request.POST, instance=self.object.address)
		else:
			context['address_form'] = self.second_form_class(instance=self.object.address)
			context['form'] = self.form_class(instance=self.object)

		return context

	def get(self, request, *args, **kwargs):
		super(EmployeeUpdate, self).get(request, *args, **kwargs)
		form = self.form_class
		address_form = self.second_form_class
		return self.render_to_response(
			self.get_context_data(
				object=self.object,
				form=form, 
				address_form=address_form
			)
		)

	def post(self, request, *args, **kwargs):
		
		self.object = self.get_object()
		form = self.form_class(self.request.POST, instance=self.object)
		address_form = self.second_form_class(self.request.POST, instance=self.object.address)
		
		if form.is_valid() and address_form.is_valid():
			return self.form_valid(form, address_form)
		else:
			return self.form_invalid(form, address_form)

	def form_valid(self, form, address_form):
		self.object = address_form.save()
		employee = form.save(commit=False)
		employee.address = self.object
		employee.save()
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form, address_form):
		return self.render_to_response(
			self.get_context_data(	
					form=form,
                    address_form=address_form
			)
		)

	def get_success_url(self):
		return reverse('employee:employee_list')

@method_decorator(login_required, name='dispatch')
class EmployeeDetails(DetailView):

	model = Employee
	template_name = 'employee/details.html'

@method_decorator(login_required, name='dispatch')
class EmployeeDelete(DeleteView):

	model = Employee
	success_url = reverse_lazy('employee:employee_list')
	template_name = 'employee/delete.html'

# Relatorio de horas por funcionario no periodo
@method_decorator(login_required, name='dispatch')
class HoursReportByTheOfficialPeriod(DetailView):

	model = Employee
	template_name = 'reports/hours_report_by_the_official_period.html'

	def get_queryset(self):
		self.queryset = super(HoursReportByTheOfficialPeriod,self).get_queryset()
		self.filtro_form=FilterForm(self.request.GET)
		self.filtro_form.is_valid()
		return self.queryset

	def get_context_data(self, **kwargs):
		context = super(HoursReportByTheOfficialPeriod,self).get_context_data(**kwargs)
		context['filtro_form']=self.filtro_form
		bank_of_hours = self.object.bank_of_hours.all()
		compensations = self.object.compensations.all()
		total_hours = self.object.bank_of_hours.aggregate(total=Coalesce(Sum('cumulative_hours'),0))['total']
		total_compensations = self.object.compensations.aggregate(total=Coalesce(Sum('amount_of_hours'),0))['total']
		if(self.filtro_form.cleaned_data.get('de',False)):
			compensations = compensations.filter(compensated_date__gte=self.filtro_form.cleaned_data['de'])
			bank_of_hours = bank_of_hours.filter(work_date__gte=self.filtro_form.cleaned_data['de'])
		if(self.filtro_form.cleaned_data.get('ate', False)):
			compensations=compensations.filter(compensated_date__lte=self.filtro_form.cleaned_data['ate'])
			bank_of_hours=bank_of_hours.filter(work_date__lte=self.filtro_form.cleaned_data['ate'])
		# Somo todas a horas extras
		hours = bank_of_hours.aggregate(total=Coalesce(Sum('cumulative_hours'),0))['total']
		context['hours']=hours
		# Somo todas as horas compensadas
		acumulated_hours = compensations.aggregate(total=Coalesce(Sum('amount_of_hours'),0))['total']
		context['acumulated_hours']=acumulated_hours #Horas acumuladas
		context['bank_of_hours']=bank_of_hours #
		context['compensations']=compensations
		context['total_hours']=total_hours
		context['total_compensations']=total_compensations
		context['total_balance']=total_hours - total_compensations
		context['balance_filter']=hours - acumulated_hours

		return context