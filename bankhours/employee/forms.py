# -*- coding: utf-8 -*-

from django import forms

from .models import *

class FunctionForm(forms.ModelForm):
	class Meta:
		model = Function
		fields = '__all__'
