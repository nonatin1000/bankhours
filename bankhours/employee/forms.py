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
		exclude = ['address']

class AddressForm(forms.ModelForm):

	class Meta:
		model = Address
		fields = '__all__'

class BankOfHoursForm(forms.ModelForm):
	
	class Meta:
		model = BankOfHours
		fields = '__all__'

class CompensationForm(forms.ModelForm):
	
	class Meta:
		model = Compensation
		fields = '__all__'