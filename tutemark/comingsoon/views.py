from django.http import HttpResponse, HttpResponseRedirect
from forms import FeedForm
from django.shortcuts import render
import datetime
from datetime import date
from models import *

# Create your views here.

def comingsoon_view(request):
	today = datetime.date.today()
	delta = date(2015, 5, 30) - today
	return render(request, 'index.html', {'days_left':delta.days})

def about_view(request):
	today = datetime.date.today()
	delta = date(2015, 5, 30) - today                        
	return render(request, 'about.html', {'days_left':delta.days} )

def contact_view(request):
	if request.method == 'POST':
		name = request.POST.get('name','')
		email = request.POST.get('email','')
		r = Response(name=name,email=email,response_time=datetime.datetime.now())
		r.save()
		today = datetime.date.today()
		delta = date(2015, 5, 30) - today
		return render(request, 'index.html', {'days_left':delta.days})
	else:
		today = datetime.date.today()
		delta = date(2015, 5, 30) - today
		return render(request, 'index.html', {'days_left':delta.days})
	
def feedback_form_view(request):
	if request.method == 'POST':
		
		form = FeedForm(request.POST)
		
		if form.is_valid():
			return HttpResponseRedirect('thanks/')
	else:
		form = FeedForm()
		
	return render(request, 'feedback_form.html', {'form': form})
	
def feedback_clean_view(request):
	if request.method == 'POST':
		
		form = FeedForm(request.POST)
		
		if form.is_valid():
			f = form.save()
			return HttpResponseRedirect('thanks/')
	else:
		form = FeedForm()
		
	return render(request, 'feedback_form.html', {'form': form})
	    
def thank_view(request):
	return render(request, 'thank.html', )
