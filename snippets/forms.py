from django import forms
from .models import Language, Snippet


class LanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = ['topping1','topping2','size']
        labels = {'topping1':'Topping 1','topping2':'Topping 2'}


class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ['']
        labels = {''}