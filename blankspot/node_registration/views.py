from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from node_registration.forms import PositionForm
from node_registration.models import Position

class PositionCreate(CreateView):
	model = Position
	success_url = reverse_lazy('thanks')

class ListPosition(View):
	model = Position
	template_name = 'list.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {'output': Position.objects.all()})
