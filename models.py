from django.db import models

# Create your models here.
class Projects(models.Model):
    
    profile = models.ImageField(upload_to='media/',blank=True)
    
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    
    
    project_name = models.CharField(max_length=255,null=True,blank=True)
    
    amount = models.FloatField(null=True,blank=True)
    status = models.CharField(max_length=255,null=True,blank=True,default='UNARCHIVED')
    