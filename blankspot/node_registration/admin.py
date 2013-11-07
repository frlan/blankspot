from django.contrib import admin
from node_registration.models import Position

class PositionAdmin(admin.ModelAdmin):
	list_display = ['nick', 'street', 'longitude', 'latitude', 'timestamp']
	search_fields = ['nick', 'street']

admin.site.register(Position, PositionAdmin)
