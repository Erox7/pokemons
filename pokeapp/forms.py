from django.forms import ModelForm
from models import *

class PokemonReviewForm(ModelForm):
    class Meta:
        model = PokemonReview
        exclude = ('user','pokemon')
