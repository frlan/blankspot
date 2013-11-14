from django.forms import ModelForm
from node_registration.models import Position

class PositionForm(ModelForm):
	model = Position
