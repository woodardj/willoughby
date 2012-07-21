from django import forms

class SearchForm(forms.Form):
  t = forms.CharField(initial='search me!')