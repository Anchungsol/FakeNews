from django.shortcuts import render,redirect
from .models import Press,Users,Record,FakeNews
from .forms import InputData,SignupForm,LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import crawling
from . import url_image_check
from .pyhanspell import check_text
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib import auth


def index(request):
   if request.method == "POST":
      form = InputData(request.POST)
      crawlings = crawling.Crawling_data()
      url_image_checks = url_image_check.Fakenews_takes()
      check_texts = check_text.Contents_check()
      if form.is_valid():
         form.cleaned_data
         count = 0
         url = request.POST['URL_Search']
         title = request.POST['News_Title']

         news_text = crawlings.get_text(url)
         news_title = crawlings.get_title(url)
         news_date = crawlings.get_date(url)
         news_imageName = crawlings.get_image(url)
         
         #count_url 점수 , press_name : 언론사 이름, press_url :언론사 url
         count_url_image,press_name,press_url = url_image_checks.url_image_Modulation(url,news_imageName)
         
         #count_date 점수 (사진 == 기사 날짜)
         count_date = url_image_checks.date_Check(news_date,news_imageName)
         
         #count_error : 맞춤법 검사 에러 수 checked_str : 맞춤법틀린거 수정 결과
         count_error,checked_str = check_texts.check_str(news_text)

         #날짜 형식 DB에 맞게 수정
         news_date = news_date.replace(" ","").replace(".","-")
         news_date = news_date[0:10]

         #count 점수별 T/F 분류
         if (count_url_image == 0):
            url_TF="False"
            image_TF="False"
         else:
            url_TF="True"
            image_TF="True"

         if (count_date == 0):
            date_TF = "False"
         else:
            date_TF = "True"

         #점수 계산 
         if (count_error > 0):
            count += 1
         count = count_url_image + count_date
         if (count >= 2):
            news_TF = True
         else:
            news_TF = False

         press = Press(pressName=press_name,pressUrl=press_url)
         press.save()
         record = Record(searchUrl=url,truth=news_TF,newsDate=news_date,content='test')
         record.save()

         fakenews = FakeNews(grammarCount=count_error,urlError=url_TF,photoError=image_TF,dateError=date_TF,score=count)
         fakenews.save()
         resultList = FakeNews.objects.last()
         return render (request, 'news/result.html',{'resultList':resultList})
   else:
      form = InputData()
      data = {
                'form' : form,
        }

   return render(request, 'news/index.html', data)

#def login(request):
#	return render(request, 'news/login.html', {})

def logins(request):
   if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['userId']
            password = login_form.cleaned_data['password']


            user = authenticate(
               username=username,
               password=password
               )

            if user:
               login(request,user)
               return HttpResponseRedirect(reverse('index'))
            login_form.add_error(None, 'ID or password X')
   else:
      login_form = LoginForm()
   context = {
      'login_form' : login_form,
   }
   return render(request, 'news/logins.html',context)





def logout(request):
   auth.logout(request)
   return HttpResponseRedirect(reverse('index'))


def signup(request):
   if request.method =="POST":
      if request.POST["password"] == request.POST["password2"]:
         user = User.objects.create_user(
            username = request.POST["userId"], password=request.POST["password"], 
            last_name = request.POST["name"], email = request.POST["email"])
      return render(request, 'news/signup.html')
   return render(request,'news/signup.html')


def record(request):
	recordList = Record.objects.all()
	newsCount = Record.objects.all().count()
	fakeCount = Record.objects.filter(truth=True).count()
	userCount = User.objects.all().count()
	return render(request, 'news/record.html', {'recordList':recordList,'newsCount':newsCount,'fakeCount':fakeCount,'userCount':userCount})


def searchboard(request):
	searchList=Record.objects.all()
	return render(request, 'news/searchboard.html',{'searchList':searchList})


def result(request):
	resultList = FakeNews.objects.last()
	return render(request, 'news/result.html',{'resultList':resultList})
