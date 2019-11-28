from django.shortcuts import render
from .models import Post

def index(request):
	return render(request, 'news/index.html', {})

def login(request):
	return render(request, 'news/login.html', {})

def signup(request):
	return render(request, 'news/signup.html',{})

def record(request):
	return render(request, 'news/record.html',{})

def searchboard(request):
	return render(request, 'news/searchboard.html',{})
