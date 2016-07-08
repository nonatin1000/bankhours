# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from .models import *
from .forms import *

class FunctionList(ListView):
	
	model = Function
	template_name = 'function/list.html'

class FunctionCreate(CreateView):

	model = Function 
	template_name = 'function/add.html'
	form_class = FunctionForm

class FunctionUpdate(UpdateView):

	model = Function
	template_name = 'function/add.html'
	form_class = FunctionForm

class FunctionDetail(DetailView):

	model = Function
	template_name = 'function/details.html'

class FunctionDelete(DeleteView):

	model = Function
	success_url = reverse_lazy('employee:function_list')
	template_name = 'function/delete.html'

class DepartmentList(ListView):

	model = Department
	template_name = 'department/list.html'

class DepartmentCreate(CreateView):

	model = Department
	template_name = 'department/add.html'
	form_class = DepartmentForm

class DepartmentUpdate(UpdateView):

	model = Department
	template_name = 'department/add.html'
	form_class = DepartmentForm

class DepartmentDetail(DetailView):

	model = Department
	template_name = 'department/details.html'

class DepartmentDelete(DeleteView):

	model = Department
	success_url = reverse_lazy('employee:department_list')
	template_name = 'department/delete.html'

class EmployeeList(ListView):

	model = Employee
	template_name = 'employee/list.html'

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

class EmployeeDetails(DetailView):

	model = Employee
	template_name = 'employee/details.html'

class EmployeeDelete(DeleteView):

	model = Employee
	success_url = reverse_lazy('employee:employee_list')
	template_name = 'employee/delete.html'

class BankOfHoursList(ListView):

	model = BankOfHours
	template_name = 'bankofhours/list.html'

class BankOfHoursCreate(CreateView):

	model = BankOfHours
	template_name = 'bankofhours/add.html'
	fields = ['employee', 'start_time', 'end_time', 'comment', 'cumulative_hours', 'work_date']

class BankOfHoursUpdate(UpdateView):

	model = BankOfHours
	template_name = 'bankofhours/add.html'
	fields = ['employee', 'start_time', 'end_time', 'comment', 'cumulative_hours', 'work_date']

class BankOfHoursDetails(DetailView):

	model = BankOfHours
	template_name = 'bankofhours/details.html'

class BankOfHoursDelete(DeleteView):

	model = BankOfHours
	success_url = reverse_lazy('employee:bank_of_hours_list')
	template_name = 'bankofhours/delete.html'

class CompensationList(ListView):

	model = Compensation
	template_name = 'compensation/list.html'

class CompensationCreate(CreateView):

	model = Compensation
	template_name = 'compensation/add.html'
	fields = ['employee', 'amount_of_hours', 'compensated_date']

class CompensationUpdate(UpdateView):

	model = Compensation
	template_name = 'compensation/add.html'
	fields = ['employee', 'amount_of_hours', 'compensated_date']

class CompensationDetails(DetailView):

	model = Compensation
	template_name = 'compensation/details.html'

class CompensationDelete(DeleteView):

	model = Compensation
	success_url = reverse_lazy('employee:compensation_list')
	template_name = 'compensation/delete.html'