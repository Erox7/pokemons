from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.template.context_processors import csrf
# Create your views here.
class PokemonDetail(DetailView):
    model = Pokemon
    template_name = 'pokemon_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PokemonDetail,self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = PokemonReview.RATING_CHOICES
        return context

        
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

def review(request,	pk):
				pokemon	= get_object_or_404(Pokemon,	pk=pk)
				if PokemonReview.objects.filter(pokemon=pokemon,	user=request.user).exists():
								PokemonReview.objects.get(pokemon=pokemon,	user=request.user).delete()
				new_review	= PokemonReview(
								rating=request.POST['rating'],
								ReviewText=request.POST['comment'],
								user=request.user,
								pokemon=pokemon)
				new_review.save()
				return HttpResponseRedirect(reverse('pokemon_detail',	args=(pokemon.id,)))
