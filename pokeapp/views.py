from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from models import *
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from forms import *
# Create your views here.

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'form.html'

class PokemonDetail(DetailView):
    model = Pokemon
    template_name = 'pokemon_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PokemonDetail,self).get_context_data(**kwargs)
        return context

class pokemonListView(ListView):
    model = Pokemon
    context_object_name = 'pokemon_list'
    template_name = 'pokemon_list.html'

class ReviewDetail(DetailView):
    model = PokemonReview
    template_name = 'review_detail.html'

class ReviewList(ListView):
    model = PokemonReview
    context_object_name = 'review_list'
    template_name = 'review_list.html'

class ReviewDelete(LoginRequiredMixin,CheckIsOwnerMixin,DeleteView):
    model = PokemonReview
    template_name = 'delete_review.html'
    success_url = reverse_lazy('pokemon_list')

class PokemonReviewCreate(LoginRequiredMixin, CreateView):
    model = PokemonReview
    template_name = 'form.html'
    form_class = PokemonReviewForm
    success_url = reverse_lazy('pokemon_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.pokemon = Pokemon.objects.get(id=self.kwargs['pk'])
        return super(PokemonReviewCreate,self).form_valid(form)

def home(request):
    template = get_template('home.html')
    variables = Context({
        'Title' : 'sPokeapp',
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
