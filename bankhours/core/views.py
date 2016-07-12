# -*- coding: utf-8 -*-

from django.shortcuts import render

# Página inicial
def index(request):
	return render(request, 'index.html')
