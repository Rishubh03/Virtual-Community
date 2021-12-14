from django import forms
from .models import Articles
from encyclopedia.models import Articles


class Search(forms.Form):
    item = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'myfieldclass', 'placeholder': 'Search'}))


class Post(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'textarea', 'image']


class Edit(forms.ModelForm):
    textarea = forms.CharField(widget=forms.Textarea(), label='')

    class Meta:
        model = Articles
        fields = ['textarea']
