from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *


class AlbumSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='pokemon-detail')
    pokemonreview_set = HyperlinkedRelatedField(many=True, read_only=True,
                                                   view_name='pokemonview-detail')


    class Meta:
        model = Pokemon
        fields = ('uri', 'name', 'type', 'description', 'pokemonreview_set')


class AlbumReviewSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='pokemonreview-detail')
    pokemon = HyperlinkedRelatedField(view_name='pokemon-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = PokemonReview
        fields = ('uri', 'ReviewText', 'user', 'userlocation', 'pokemon')
