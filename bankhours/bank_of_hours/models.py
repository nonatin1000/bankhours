# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from bankhours.employee.models import *

class AuditModel(models.Model):
	# Audit Fields
	created_on = models.DateTimeField('Criado em', auto_now_add=True)
	updated_on = models.DateTimeField('Autalizado em', auto_now=True)

	class Meta:
		abstract=True
		
class BankOfHours(AuditModel):
	employee = models.ForeignKey(Employee, verbose_name='Funcionário', related_name='bank_of_hours', on_delete=models.CASCADE)
	start_time = models.TimeField('Hora de Entrada', help_text='*')
	end_time = models.TimeField('Hora de Saída', help_text='*')
	cumulative_hours = models.CharField('Horas', max_length=100, help_text='*')
	comment = models.CharField('Observação', max_length=100, blank=True, null=True)
	work_date = models.DateTimeField('Data',  help_text='*')
	
	class Meta:
		verbose_name = 'Banco de Hora'
		verbose_name_plural = 'Banco de Horas'
		ordering = ['-id']


	def __str__(self):
		return "{} - {} - {}".format(self.work_date, self.start_time, self.end_time)

	def get_absolute_url(self):
		return reverse('bank_of_hours:bank_of_hours_list')

class Compensation(AuditModel):
	employee = models.ForeignKey(Employee, verbose_name='Funcionário', related_name='compensations', on_delete=models.CASCADE)
	amount_of_hours = models.CharField('Horas Compensadas', max_length=100, help_text='*')
	bank_of_hours = models.ManyToManyField(BankOfHours, verbose_name='Banco de Horas', related_name='compensations')
	compensated_date = models.DateTimeField('Data',  help_text='*')
	
	class Meta:
		verbose_name = 'Compensação'
		verbose_name_plural = 'Compensações'
		ordering = ['-id']

	def get_absolute_url(self):
		return reverse('bank_of_hours:compensation_list')
