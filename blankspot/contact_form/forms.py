from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage


class ContactForm(forms.Form):
    subject = forms.CharField(label="Betreff", max_length=100)
    sender = forms.EmailField(label="Emailadresse")
    message = forms.CharField(label="Botschaft", widget=forms.Textarea)


    def send_email(self):
        print settings.ROOT_URLCONF
        email = EmailMessage(
                    subject="foo",
                    #body='Here is the message.',
                    from_email='foo@example.com',
                    to=['foo@example.com'])

        values = []
        for i in self.fields.iteritems():
            values.append("%s: \t%s" % (self[i[0]].label, str(self.cleaned_data[i[0]]) ) )

        email.send()

