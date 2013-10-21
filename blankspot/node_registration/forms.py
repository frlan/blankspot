from django import forms
from django.forms import ModelForm
from node_registration.models import Position

class ContactForm(forms.Form):
	name = forms.CharField()
	message = forms.CharField(widget=forms.Textarea)

	def send_email(self):
		# send email using the self.cleaned_data dictionary
		pass

class PositionForm(ModelForm):
	model = Position
	exclude = ('Nick')
		#exclude = ('slug', 'author', 'date_created', 'date_updated')
