  
from django.db import models


class BaseModel(models.Model):
    
    id = models.AutoField(primary_key = True)
    created_date = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
    modified_date = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)

    class Meta:
        
        abstract = True
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'