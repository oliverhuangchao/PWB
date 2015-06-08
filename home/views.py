from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader, Context
# Create your views here.

def index(req):
	return render(req,'homepage.html',{'title':'Chao\'s homepage','name':'chaoh'})
	#return render_to_response('index.html',{'title':'hello','id':'abcdefg'}) 

def contract(req):
	return render(req,'contract.html',{'title':'Contract information'})

def work(req):
	return render(req,'work.html',{'title':'My Working experience'})

def projects(req):
	return render(req,'projects.html',{'title':'Previous Projects'})