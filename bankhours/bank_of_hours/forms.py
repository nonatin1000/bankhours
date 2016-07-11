# -*- coding: utf-8 -*-

from django import forms
from .models import *
from dal import autocomplete

class BankOfHoursForm(forms.ModelForm):
	
	class Meta:
		model = BankOfHours
		fields = '__all__'
		widgets = {'employee': autocomplete.ModelSelect2(url='employee:employee_autocomplete')}

class CompensationForm(forms.ModelForm):
	
	class Meta:
		model = Compensation
		fields = '__all__'
		widgets = {
			'bank_of_hours': autocomplete.ModelSelect2Multiple(url='bank_of_hours:bank_of_hours_autocomplete', forward=['employee']),
			'employee': autocomplete.ModelSelect2(url='employee:employee_autocomplete')
			}
