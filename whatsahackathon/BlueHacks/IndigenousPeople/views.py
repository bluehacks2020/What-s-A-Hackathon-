from django.shortcuts import render
from django.http import HttpResponse
from .models import CultureInfo
from .models import Product1
from .models import Product2
from .models import Product3

def ips1(request):
	products = Product1.objects.all()
	cultures = CultureInfo.objects.get(name="Ateneans")
	return render(request, 'ips1.html', {'products' : products, 'cult_name' : cultures.name, 'pic1' : cultures.pic1, 'pic2' : cultures.pic2, 'pic3' : cultures.pic3})


def ips2(request):
	products = Product2.objects.all()
	cultures = CultureInfo.objects.get(name="Indigenous People A")
	return render(request, 'ips2.html', {'products' : products, 'cult_name' : cultures.name, 'pic1' : cultures.pic1, 'pic2' : cultures.pic2, 'pic3' : cultures.pic3})


def ips3(request):
	products = Product3.objects.all()
	cultures = CultureInfo.objects.get(name="Dumagat-Remontado")
	return render(request, 'ips3.html', {'products' : products, 'cult_name' : cultures.name, 'pic1' : cultures.pic1, 'pic2' : cultures.pic2, 'pic3' : cultures.pic3})