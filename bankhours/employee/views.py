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