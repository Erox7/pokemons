"""pokemons URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from pokeapp.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/register/$', register),
    url(r'^home/$', home),
    url(r'^$', home),
    url(r'^reviews/$',ReviewList.as_view(), name = 'review_list',),
    url(r'^reviews/(?P<pk>\d+)/details/$', ReviewDetail.as_view(), name ='review_detail'),
    url(r'^reviews/(?P<pk>\d+)/delete/$', ReviewDelete.as_view(), name = 'review_delete'),
    url(r'^pokemons/$',pokemonListView.as_view(), name = 'pokemon_list',),
    url(r'^pokemons/(?P<pk>\d+)/details/reviewcreate/$', PokemonReviewCreate.as_view(), name ='review_create'),
    url(r'^pokemons/(?P<pk>\d+)/details/$',PokemonDetail.as_view(), name ='pokemon_detail'),
    url(r'^review/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=PokemonReview,
           template_name='form.html',
           success_url='/reviews',
            form_class=PokemonReviewForm),
        name='review_edit'),
]


urlpatterns += [
    url(r'^api/pokemons/$',
        APIPokemonList.as_view(), name='pokemon-list'),
    url(r'^api/pokemons/(?P<pk>\d+)/$',
        APIPokemonDetail.as_view(), name='pokemon-detail'),
    url(r'^api/pokemonreviews/$',
        APIPokemonReviewList.as_view(), name='pokemonreview-list'),
    url(r'^api/pokemonreviews/(?P<pk>\d+)/$',
        APIPokemonReviewDetail.as_view(), name='pokemonreview-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'xml'])
