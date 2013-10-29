from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from node_registration.forms import PositionForm
from node_registration.models import Position
from django.shortcuts import render
from django.views.generic.base import View

class ContactView(FormView):
	template_name = 'contact.html'
	success_url = '/thanks/'

	def form_valid(self, form):
		# This method is called when valid form data has been POSTed.
		# It should return an HttpResponse.
		form.send_email()
		return super(ContactView, self).form_valid(form)

class PositionCreate(CreateView):
	model = Position

class PositionUpdate(UpdateView):
	model = Position

class PositionDelete(DeleteView):
	model = Position
	success_url = reverse_lazy('position-list')

class ListPosition(View):
	model = Position
	template_name = 'list.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {'output': Position.objects.all()})

