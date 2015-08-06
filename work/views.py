from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader, Context
# Create your views here.


def workClemson(req):
	return render(req,'../../work/templates/workClemson.html',{'tilte':'RA in CLemson'})