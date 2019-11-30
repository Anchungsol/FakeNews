

from django import forms

class InputData(forms.Form):
	URL_Search = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'URL search'}))
	News_Title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'News Title'}))
