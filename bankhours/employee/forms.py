# -*- coding: utf-8 -*-

from django import forms
from .models import *
from localflavor.br.forms import BRCPFField

class FunctionForm(forms.ModelForm):
	
	class Meta:
		model = Function
		fields = '__all__'

class DepartmentForm(forms.ModelForm):

	class Meta:
		model = Department
		fields = '__all__'

class EmployeeForm(forms.ModelForm):

	cpf = BRCPFField(label='CPF', required=True)

	class Meta:
		model = Employee
		exclude = ['address']

class AddressForm(forms.ModelForm):

	class Meta:
		model = Address
		fields = '__all__'

class FilterForm(forms.Form):
	de = forms.DateField(label='De',required=False)
	ate = forms.DateField(label='Até',required=False)