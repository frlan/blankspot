from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):
    subject = forms.CharField(label=_("Subject"), max_length=100)
    sender = forms.EmailField(label=_("Email"))
    message = forms.CharField(label=_("Message"), widget=forms.Textarea)

    def send_email(self):

        values = []
        for i in self.fields.iteritems():
            values.append("%s: \t%s" % (self[i[0]].label, str(self.cleaned_data[i[0]]) ) )

        email = EmailMessage(
                    subject="foo",
                    body="\n".join(values),
                    from_email=self.cleaned_data['sender'],
                    to=['foo@example.com'])

        email.send()

