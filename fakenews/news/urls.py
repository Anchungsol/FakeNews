
from django.urls import path
from . import views

urlpatterns = [

	path('',views.index,name='index'),
	path('index/',views.index),
	path('logins/',views.logins,name='logins'),
	path('signup/',views.signup,name='signup'),
	path('record/',views.record,name='record'),
	path('searchboard/',views.searchboard,name='searchboard'),
	path('result/',views.result,name='result'),
	path('logout/',views.logout,name='logout'),
]

