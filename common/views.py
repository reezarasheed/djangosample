from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import contactus
from .forms import ContactUsForm

def homepage(request):

  template=loader.get_template('form.html')
  data ={ }
  return HttpResponse(template.render(data,request))



def contactpage (req):
    template = loader.get_template("contact.html")
    mycontactform = ContactUsForm()
    data = {"forms": mycontactform}
    return HttpResponse(template.render(data, req))

def resultpage (req):
 template = loader.get_template("result.html")

 data= {"year": 2015,
        "name": "Anil",
        "mark" : 450,
        "status": "PASS"}

 return HttpResponse(template.render(data, req))
