from .models import Users
from django import forms

class InputData(forms.Form):
   URL_Search = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control col-lg-20 col-xl-50','placeholder':'URL search'}))
   News_Title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control col-lg-20 col-xl-50','placeholder':'News Title'}))

class SignupForm(forms.Form):
   userId = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ID'}))
   password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'PassWord'}))
   email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
   name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))

class LoginForm(forms.Form):
   userId = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ID'}))
   password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'PassWord'}))

