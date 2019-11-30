from django.shortcuts import render
from .models import Post
from .forms import InputData
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
	
	if request.method == "POST":
		form = InputData(request.POST)
		if form.is_valid():
			form.cleaned_data
			title = request.POST['URL_Search']
			url = request.POST['News_Title']
			return HttpResponseRedirect(reverse('result'))
	else:
		form = InputData()


	data = {
		'form' : form,
	}	

	return render(request, 'news/index.html', data)

def login(request):
	return render(request, 'news/login.html', {})

def signup(request):
	return render(request, 'news/signup.html',{})

def record(request):
	return render(request, 'news/record.html',{})

def searchboard(request):
	return render(request, 'news/searchboard.html',{})

def result(request):
	return render(request, 'news/result.html',{})
