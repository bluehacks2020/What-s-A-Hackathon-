
from django.urls import path
from . import views


urlpatterns = [
	path('1', views.ips1),
	path('2', views.ips2),
	path('3', views.ips3)
]