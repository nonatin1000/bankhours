# -*- coding: utf-8 -*-

from django import forms
from .models import *
from dal import autocomplete
from django.db.models import Sum
from django.db.models.functions import Coalesce

class BankOfHoursForm(forms.ModelForm):
	
	class Meta:
		model = BankOfHours
		fields = '__all__'
		widgets = {'employee': autocomplete.ModelSelect2(url='employee_autocomplete')}

class CompensationForm(forms.ModelForm):
	
	# Validação na compensação de horas do funcionario
	def clean_amount_of_hours(self):
		employee = self.cleaned_data['employee']
		# Somo todas a horas extras
		hours = BankOfHours.objects.filter(employee=employee).aggregate(total=Coalesce(Sum('cumulative_hours'),0))['total']
		# Somo todas as horas compensadas
		acumulated_hours = Compensation.objects.filter(employee=employee).aggregate(total=Coalesce(Sum('amount_of_hours'),0))['total']
		print(hours)
		if self.cleaned_data['amount_of_hours'] > (hours-acumulated_hours):
			raise forms.ValidationError('Esse funcionário não possui horas suficientes para ser compensadas')
		return self.cleaned_data['amount_of_hours']

	class Meta:
		model = Compensation
		fields = '__all__'
		widgets = {
			'employee': autocomplete.ModelSelect2(url='employee_autocomplete')
			}

class FilterForm(forms.Form):
	de = forms.DateField(label='De',required=False)
	ate = forms.DateField(label='Até',required=False)