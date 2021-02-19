from django import forms
from .models import Language, Snippet

class LanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = ['name','slug']


class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ['name', 'description', 'snippet', 'language', 'public']