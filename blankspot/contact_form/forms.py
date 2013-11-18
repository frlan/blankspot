from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()


    def send_email(self):

        email = EmailMessage(
                    subject=self.cleaned_data[subject],
                    #body='Here is the message.',
                    from_email='flanitz@bgc-jena.mpg.de',
                    to=['frank.lanitz@bgc-jena.mpg.de'])

        values = []
        for i in self.fields.iteritems():
            values.append("%s: \t%s" % (self[i[0]].label, str(self.cleaned_data[i[0]]) ) )

        email.send()
