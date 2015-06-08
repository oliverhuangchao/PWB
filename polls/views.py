from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader, Context

# Create your views here.
class Person(object):
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex
	def say(self):
		return "I'm " + self.name

def index(req,id):
	#return HttpResponse('<h1>hello world</h1>')
	#user = {'name':'tom','age':23,'sex':'male'}
	user = Person('hello',100,'male')
	book_list = {'python','java','php','web'}
	return render_to_response('index.html',{'title':'hellotwigfunc','book_list':book_list,'user':user}) 
	# t = loader.get_template('index.html')
	# c = Context({})
	# return HttpResponse(t.render(c))
