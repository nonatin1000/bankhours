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
	
	template_name = 'function/list.html'
	model = Function

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
	success_url = reverse_lazy('employee:list')
	template_name = 'function/delete.html'
