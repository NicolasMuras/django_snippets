from django.contrib import admin

from .models import Language, Snippet
from user.models import User


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass