from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.template import loader

def contenidoHTML(request):
	return render(request, 'Home.html')

def PlantillaHija(request):
	plantillaExterna = loader.get_template('PlantillaHija.html')
	documento = plantillaExterna.render()
	return HttpResponse(documento)

def PlantillaHija2(request):
	plantillaExterna = loader.get_template('PlantillaHija2.html')
	documento = plantillaExterna.render()
	return HttpResponse(documento)

def Home(request):
	plantillaExterna = loader.get_template('Home.html')
	documento = plantillaExterna.render()
	return HttpResponse(documento)

def ChatBoxInteractivo(request):
	plantillaExterna = loader.get_template('ChatBoxInteractivo.html')
	documento = plantillaExterna.render()
	return HttpResponse(documento)
