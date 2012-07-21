from django.shortcuts import render_to_response
from netflix import *
from imdb import *
from forms import *
# Create your views here.

def homepage(request):
  if 't' in request.GET:
    form = SearchForm(request.GET)
    imdb = ImdbLookup()
    flix = NetflixChecker()
    
    if form.is_valid():
      movie_data = imdb.search(form.cleaned_data['t'])

      data = flix.availability(movie_data['Title'])

      print data
      return render_to_response('homepage/results.html',{'form':form,'data':data})
  else:
    s = SearchForm()
    return render_to_response('homepage/homepage.html',{'form':s})
    
