from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader, Context
from django.core.mail import send_mail
import os
import render_preparation

# Create your views here.
def prepare_to_render():
	return 


def index(req):
	return render(req,'newindex.html',{'title':'Chao\'s homepage','subtitle':'Basic Introduction','name':'chaoh','title_pic':'chaoh.jpg','sidebar_contents':['About','Work','Project','Contract']})
	#return render_to_response('index.html',{'title':'hello','id':'abcdefg'}) 

def ra_work(req):
        return render(req,'ra.html',{'title':'Research Assistant','subtitle':'Research Assistant in Clemson','name':'chaoh','title_pic':'clemson.jpg','sidebar_contents':['Searching Building','DNA Indexing']})

def bd_majoraide(req):
		#send_mail('my django example', 'main contents in django!', 'chaoh@g.clemson.edu.com',['oliverhuangchao@gmail.com'], fail_silently=False)
		return render(req,'majoraide.html',{'title':'Backend Developer','subtitle':'Backend Developer in Majoraide','name':'chaoh','title_pic':'majoraide.png','sidebar_contents':['Major Duty','Pomodoro Design']})

