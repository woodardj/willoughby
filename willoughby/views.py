from django.shortcuts import render_to_response
from netflix import *
from imdb import *
from amazon import *
from forms import *
# Create your views here.

def homepage(request):
  if 't' in request.GET:
    form = SearchForm(request.GET)

    
    if form.is_valid():
      imdb = ImdbLookup()
      flix = NetflixChecker()
      amazon = AmazonChecker()
      
      movie_data = imdb.search(form.cleaned_data['t'])

      avail = []

      avail.extend(flix.availability(movie_data['Title']))
      avail.extend(amazon.availability(movie_data['Title']))
      
      

      return render_to_response('homepage/results.html',{'form':form,'movie':movie_data,'avail':avail})
  else:
    s = SearchForm()
    return render_to_response('homepage/homepage.html',{'form':s})
    
