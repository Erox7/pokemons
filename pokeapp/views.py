from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.template.context_processors import csrf
# Create your views here.

def home(request):
    template = get_template('home.html')
    variables = Context({
        'Title' : 'Pokeapp',
        'user' : request.user
    })
    page = template.render(variables)

    return HttpResponse(page)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login')
    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/htmlregister.html', token)
