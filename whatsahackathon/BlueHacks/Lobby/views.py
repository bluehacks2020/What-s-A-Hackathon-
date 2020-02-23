from django.shortcuts import render
from .models import Exhibition


def index(request):
	exhibit = Exhibition.objects.all()
	return render(request, 'index.html', {'exhibit' : exhibit})
