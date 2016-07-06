# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class AuditModel(models.Model):
	# Audit Fields
	created_on = models.DateTimeField('Criado em', auto_now_add=True)
	updated_on = models.DateTimeField('Autalizado em', auto_now=True)

	class Meta:
		abstract=True

class Function(AuditModel):
	name = models.CharField('Nome', max_length=100, help_text='*')
	description = models.CharField('Descrição', max_length=100, blank=True)

	def __str__(self):
		return name

	def get_absolute_url(self):
		return reverse('employee:list')

	class Meta:
		verbose_name = 'Função'
		verbose_name_plural = 'Funções'
		ordering = ['-id']