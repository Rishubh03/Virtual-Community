from django.forms import widgets
from  .models import Question, Response

from django import forms 

class Search(forms.Form):
    item = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'myfieldclass', 'placeholder': 'Search'}))

class NewQuestion(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'body']
		widgets = {
			'title': forms.TextInput(attrs={
				'autofocus':'True',
				'placeholder':'Ask a Question?'
			})
		}

class NewResponseForm(forms.ModelForm):
	class Meta:
		model = Response
		fields = ['body']

class NewReplyForm(forms.ModelForm):
	class Meta:
		model = Response
		fields = ['body']
		widgets = {
			'body': forms.Textarea(attrs={
				'row':2,
				'placeholder':'What are your thoughts?'
			})
		}
