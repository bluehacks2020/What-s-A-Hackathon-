from django.contrib import admin
from .models import Exhibition


class ExhibitionAdmin(admin.ModelAdmin):
	list_display = ('culture', 'short_description')

admin.site.register(Exhibition, ExhibitionAdmin)