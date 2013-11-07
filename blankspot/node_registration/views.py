from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from node_registration.forms import PositionForm
from node_registration.models import Position
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.views.generic.base import View
from django.utils.translation import ugettext as _

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
    success_url = reverse_lazy('thanks')

    def form_valid(self, form):
        # TODO:
        # Maybe moving the email stuff into a seperate function.

        # Creating the body of the message
        values = []

        for i in form.fields.iteritems():
                values.append("%s: \t%s" % (i[0],form.data[i[0]]))

        # Building up email object with actual content.
        email = EmailMessage(
                    subject="Blankspot: A new position has been added",
                    from_email='foo@example.com',
                    body="\n".join(values),
                    to=['foo@example.com'])
        # Sending out email.
        email.send()

        return super(PositionCreate, self).form_valid(form)


class ListPosition(View):
    model = Position
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'output': Position.objects.all()})
