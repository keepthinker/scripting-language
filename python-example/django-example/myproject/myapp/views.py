# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from myapp.models import Dreamreal

def hello(request):
	text = "<html><body>hello world!</body></html>"
	return HttpResponse(text)

def morning(request):
	return render(request, "morning.html", {})

def param(request, param):
	text = "<html><body>Param is %s </body></html>"%param
	return HttpResponse(text)

def date_display(request, month, year):
	text = "<html><body>The date is %s/%s</body></html>"%(month, year)
	return HttpResponse(text)

def today(request):
	date = datetime.now().date()
	daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	return render(request, "today.html", {"today": date, "daysOfWeek": daysOfWeek})


def crudops(request):
   #Creating an entry
   
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   
   #Read ALL entries
   objects = Dreamreal.objects.all()
   res ='Printing all Dreamreal entries in the DB : <br>'
   
   for elt in objects:
      res += elt.name+"<br>"
   
   #Read a specific entry:
   sorex = Dreamreal.objects.get(name = "sorex")
   res += 'Printing One entry <br>'
   res += sorex.name
   
   #Delete an entry
   res += '<br> Deleting an entry <br>'
   sorex.delete()
   
   #Update
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   res += 'Updating entry<br>'
   
   dreamreal = Dreamreal.objects.get(name = 'sorex')
   dreamreal.name = 'thierry'
   dreamreal.save()
   
   return HttpResponse(res)

