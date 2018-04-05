from django import forms
from models import Feedbacks

class FeedForm(forms.ModelForm):

    class Meta:
    	model = Feedbacks
    	fields = ['name', 'message']
