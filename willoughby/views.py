from django.shortcuts import render_to_response
# Create your views here.

def homepage(request):
  return render_to_response('homepage/homepage.html',{})