# -*- coding: utf-8 -*-

from django import forms

from .models import *

class FunctionForm(forms.ModelForm):
	
	class Meta:
		model = Function
		fields = '__all__'

class DepartmentForm(forms.ModelForm):

	class Meta:
		model = Department
		fields = '__all__'

class EmployeeForm(forms.ModelForm):

	class Meta:
		model = Employee
		fields = '__all__'