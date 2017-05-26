from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *


class PokemonSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='pokemon-detail')
    pokemonreview_set = HyperlinkedRelatedField(many=True, read_only=True,
                                                   view_name='pokemonreview-detail')


    class Meta:
        model = Pokemon
        fields = ('uri', 'name', 'description', 'pokemonreview_set')


class PokemonReviewSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='pokemonreview-detail')
    pokemon = HyperlinkedRelatedField(view_name='pokemon-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = PokemonReview
        fields = ('uri', 'ReviewText', 'user', 'userlocation', 'pokemon')
