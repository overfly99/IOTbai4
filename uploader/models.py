
# Create your models here.
from django.db import models

class DropBox(models.Model):
    title = models.CharField(max_length=30)
    document = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        verbose_name_plural = 'Drop Boxes'




      