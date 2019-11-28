
from django.urls import path
from . import views

urlpatterns = [

	path('',views.index,name='index'),
	path('index/',views.index),
	path('login/',views.login,name='login'),
	path('signup/',views.signup,name='signup'),
	path('record/',views.record,name='record'),
	path('searchboard/',views.searchboard,name='searchboard'),

]

