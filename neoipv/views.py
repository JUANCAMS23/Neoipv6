from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def bienvenida(request):
	return HttpResponse("Bienvenido a esta pagina")

def bienvenidaRojo(request): # Pasamos un objeto de tipo request como primer argumento.
	return HttpResponse("<p style='color: red;'>Bienvenido o bienvenida a este curso de Django. ;)</p>")

def contenidoHTML(request):
	plantillaExterna = open("C:/neoipv/neoipv/plantillas/plantilla.html")
	template = Template(plantillaExterna.read())
	plantillaExterna.close()
	contexto = Context()
	documento = template.render(contexto)
	return HttpResponse(documento)

def contenidoHTMLCargadores(request):
	plantillaExterna = loader.get_template('plantilla2.html')
	documento = plantillaExterna.render()
	return HttpResponse(documento)

def PlantillaHija(request):
	plantillaExterna = loader.get_template('PlantillaHija.html')
	documento = plantillaExterna.render()
	return HttpResponse(documento)

def PlantillaHija2(request):
	plantillaExterna = loader.get_template('PlantillaHija2.html')
	documento = plantillaExterna.render()
	return HttpResponse(documento)

def Home(request):
	plantillaExterna = loader.get_template('../Home.html')
	documento = plantillaExterna.render()
	return HttpResponse(documento)

def AcercaDeNosotros(request):
	plantillaExterna = loader.get_template('AcercaDeNosotros.html')
	documento = plantillaExterna.render()
	return HttpResponse(documento)

def ChatBoxInteractivo(request):
	plantillaExterna = loader.get_template('ChatBoxInteractivo.html')
	documento = plantillaExterna.render()
	return HttpResponse(documento)
