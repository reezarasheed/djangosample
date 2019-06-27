
from django.http import HttpResponse
from django.template import loader

def homepage(request):

  template=loader.get_template('form.html')
  data ={ }
  return HttpResponse(template.render(data,request))

