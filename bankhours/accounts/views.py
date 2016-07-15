from django.shortcuts import render, redirect, get_object_or_404
from .forms import EditAccountForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

@login_required
def edit(request):
	template_name = "accounts/edit.html"
	context = {}
	if request.method == "POST":
		form = EditAccountForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, "Os dados da conta foram alterados com sucesso")
			return redirect("core:index")
	else:
		form = EditAccountForm(instance=request.user)

	context['form'] = form
	return render(request, template_name, context)
