from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView,DetailView

from .models import Language, Snippet
from .forms import SnippetForm
from user.models import User


class Index(TemplateView):
    template_name = 'index.html'


class ListSnippet(ListView):
    model = Snippet
    template_name = 'snippets/user_snippets.html'
    queryset = Snippet.objects.filter(public = True)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(self.template_name)
        else:
            return redirect('login')

class DetailSnippet(DetailView):
    modele = Snippet
    success_url = reverse_lazy('snippets:snippet')

class UpdateSnippet(UpdateView):
    model = Snippet
    form_class = SnippetForm
    template_name = 'snippets/snippet_edit.html'


class CreateSnippet(CreateView):
    model = Snippet
    form_class =  SnippetForm
    template_name = 'snippets/snippet_add.html'
    success_url = reverse_lazy('snippets:index')


class DeleteSnippet(DeleteView):
    model = Snippet

    def post(self,request,pk,*args,**kwargs):
        objecto = Snippet.objects.get(id = pk)
        objecto.estado = False
        objecto.save()
        return redirect('snippet:user_snippets')


def login(request):
    return render(request, 'login.html', {})


def logout(request):
    return render(request, 'login.html', {})


# def index(request):
#     return render(request, 'index.html', {})


def language(request):
    return render(request, 'index.html', {})


# def user_snippets(request):
#     return render(request, 'snippets/user_snippets.html', {})


# def snippet(request):
#     return render(request, 'snippets/snippet.html', {})


# def snippet_add(request):
#     return render(request, 'snippets/snippet_add.html', {})


# def snippet_edit(request):
#     return render(request, 'snippets/snippet_add.html', {})


# def snippet_delete(request):
#     return render(request, 'snippets/user_snippets.html', {})
