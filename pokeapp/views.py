from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    template = get_template('home.html')
    variables = Context({
        'Title' : 'Pokeapp',
        'user' : request.user
    })
    page = template.render(variables)

    return HttpResponse(page)
