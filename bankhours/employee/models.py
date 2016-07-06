# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
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
	description = models.TextField('Descrição', blank=True, null=True)

	def __str__(self):
		return name

	def get_absolute_url(self):
		return reverse('employee:function_list')

	class Meta:
		verbose_name = 'Função'
		verbose_name_plural = 'Funções'
		ordering = ['-id']

class Department(AuditModel):
	name = models.CharField('Nome', max_length=100, help_text='*')
	description = models.TextField('Descrição', blank=True, null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('employee:department_list')

	class Meta:
		verbose_name = 'Departamento'
		verbose_name_plural = 'Departamentos'
		ordering = ['-id']

class Employee(AuditModel):

	name = models.CharField('Nome Completo', max_length=100, help_text='*')
	MALE = 'M'
	FEMALE  = 'F'
	SEX_CHOICES = ((MALE, 'Masculino'), (FEMALE, 'Feminino'),)
	sex = models.CharField('Sexo', max_length=1, choices=SEX_CHOICES, default=FEMALE, help_text='*')
	
	def is_upperclass(self):
		return self.sex in (self.MALE, self.FEMALE)

	MARRIED = 'CASADO'
	SINGLE = 'SOLTEIRO'
	SEPARATED = 'SEPARADO'
	WINDOWER = 'VIUVO'
	DIVORCED = 'DIVORCIADO'
	MARITAL_STATUS_CHOICES = ((MARRIED, 'Casado'), (SINGLE, 'Solteiro'), (SEPARATED, 'Separado'), (WINDOWER, 'Viúvo'), (DIVORCED, 'Divorciado'),)
	marital_status = models.CharField('Estado Cívil', max_length=10, choices=MARITAL_STATUS_CHOICES, default=SINGLE, help_text='*')
	
	def is_upperclass(self):
		return self.marital_status in (self.MARRIED, self.SINGLE, self.SEPARATED, self.WINDOWER, self.DIVORCED)

	birth_date = models.DateField('Data Nascimento', help_text='*')
	siape = models.IntegerField('Siape', help_text='*')
	phone = models.CharField('Telefone', max_length=16, blank=True, null=True)
	email = models.EmailField('E-mail', blank=True, null=True)
	function = models.ForeignKey(Function, verbose_name='Função', related_name='employees_functions')
	department = models.ForeignKey(Department, verbose_name='Departamento', related_name='employees_departments')
	address = GenericRelation('Address')

	def __str__(self): 
		return self.name

class Address(AuditModel):
	country = models.CharField('País', max_length=255, default='Brasil')
	UF_CHOICES = (
	    ('AC', 'Acre'), 
	    ('AL', 'Alagoas'),
	    ('AP', 'Amapá'),
	    ('BA', 'Bahia'),
	    ('CE', 'Ceará'),
	    ('DF', 'Distrito Federal'),
	    ('ES', 'Espírito Santo'),
	    ('GO', 'Goiás'),
	    ('MA', 'Maranão'),
	    ('MG', 'Minas Gerais'),
	    ('MS', 'Mato Grosso do Sul'),
	    ('MT', 'Mato Grosso'),
	    ('PA', 'Pará'),
	    ('PB', 'Paraíba'),
	    ('PE', 'Pernanbuco'),
	    ('PI', 'Piauí'),
	    ('PR', 'Paraná'),
	    ('RJ', 'Rio de Janeiro'),
	    ('RN', 'Rio Grande do Norte'),
	    ('RO', 'Rondônia'),
	    ('RR', 'Roraima'),
	    ('RS', 'Rio Grande do Sul'),
	    ('SC', 'Santa Catarina'),
	    ('SE', 'Sergipe'),
	    ('SP', 'São Paulo'),
	    ('TO', 'Tocantins')
	)
	state = models.CharField('UF', max_length=2, choices=UF_CHOICES, default='PI')
	city = models.CharField('Cidade', max_length=255)
	street = models.CharField('Logradouro',max_length=255)
	neighborhood = models.CharField('Bairro', max_length=255)
	number = models.CharField('Número', max_length=20)
	zip_code = models.CharField('CEP', max_length=10, blank=True, null=True)
	complement = models.CharField('Complemento', max_length=255, blank=True, null=True)
	reference_point = models.CharField('Ponto de Referência', max_length=255, blank=True, null=True)
	
	# Generic Relation
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField(db_index=True)
	content_object = GenericForeignKey('content_type', 'object_id')