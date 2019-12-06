from django.db import models
from django.urls import reverse

class MarcTemplate(models.Model):
    MarcTemplateTitle= models.CharField(max_length=200)
    biblio_type_id= models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    jsonObject = models.TextField()
 
    #def get_absolute_url(self):
    #    return reverse('main:marctemplatelist')