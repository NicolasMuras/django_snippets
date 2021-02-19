from django.urls import path, include
from .forms import SnippetForm
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('snippets/python/', views.language, name='language'),

    path('snippets/user/juancito/', views.ListSnippet.as_view(), name='user_snippets'),
    path('snippets/snippet/<int:pk>', views.DetailSnippet.as_view(), name='snippet'),
    path('snippets/add/', views.CreateSnippet.as_view(), name='snippet_add'),
    path('snippets/edit/<int:pk>', views.UpdateSnippet.as_view(), name='snippet_edit'),
    path('snippets/delete/<int:pk>', views.DeleteSnippet.as_view(), name='snippet_delete'),
    # path('snippets/user/juancito/', views.user_snippets, name='user_snippets'),
    # path('snippets/snippet/', views.snippet, name='snippet'),
    # path('snippets/add/', views.snippet_add, name='snippet_add'),
    # path('snippets/edit/', views.snippet_edit, name='snippet_edit'),
    # path('snippets/delete/', views.snippet_delete, name='snippet_delete'),
]