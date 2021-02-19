from __future__ import unicode_literals

from user.models import User

from django.db import models


class Language(models.Model):

    name = models.CharField(max_length=50, null = False)
    slug = models.CharField(max_length=50, null = False)

    class Meta:
        verbose_name = 'Lenguaje'
        verbose_name_plural = 'Lenguajes'

    def __str__(self):
        return self.name

class Snippet(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Usuario', null = False)
    created_date = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    name = models.CharField(max_length=255, null = False)
    description = models.TextField()
    snippet = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name = 'Lenguaje', null = False)
    public = models.BooleanField(default = False)

    class Meta:
        verbose_name = 'Snippet'
        verbose_name_plural = 'Snippets'

    def __str__(self):
        return self.name