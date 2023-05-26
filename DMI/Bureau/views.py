from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Bureau
# Create your views here.

def Bureau(request):
    myaffiliates = Bureau.objects.all().values()
    template = loader.get_template('all_affiliates.html')
    return HttpResponse (template.render(context, request))

def details(reguest, id):
    myaffiliates = Bureau.objects.get(id=id)
    template  = loader.get_template('details.html')
    context = {
        'myaffiliates':myaffiliates
    }
    return HttpResponse(template.render(context, request))
