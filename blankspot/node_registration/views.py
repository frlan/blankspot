from django.http import HttpResponse
from node_registration.models import position
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

def index(request):
    node_list = position.objects.all()
    output = ', '.join([p.street for p in node_list])
    return HttpResponse(output)

def list_nodes(request):
    return render(request, 'list.html', {'output':position.objects.all()})
