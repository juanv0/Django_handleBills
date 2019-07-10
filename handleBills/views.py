from django.shorcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("<H2>Hey! Welcome to edureka! </H2>")

