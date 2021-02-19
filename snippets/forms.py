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
        labels = {
            'name': 'Nombre del snippet',
            'description': 'Descripción',
            'snippet': 'Introduce el código',
            'language': 'Introduce el lenguaje',
            'public': 'Visibilidad',
        }
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese el nombre del snippet'
                }
            )
            'description': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese una descripción'
                }
            )
            'snippet': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese el código'
                }
            )
            'language': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Lenguaje utilizado'
                }
            )
            'public': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Visibilidad'
                }
            )
        }
