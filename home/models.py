from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    decr = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name

class Recruitment(models.Model):
    sno=models.AutoField(primary_key=True)
    orgName=models.CharField(max_length=250)
    slug=models.CharField(max_length=100,default='')
    content=models.TextField()
    cgpareq=models.FloatField(null=True, blank=True, default=None)
    user=models.ManyToManyField(User, blank=True, null=True)
    date=models.DateField()
    def __str__(self):
        return self.orgName
    
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    fname=models.CharField(max_length=30,default='')
    lname=models.CharField(max_length=30,default='')
    roll = models.IntegerField( blank=True)
    address=models.TextField()
    branch=models.TextField()
    sem=models.IntegerField(null=True, blank=True, default=None)
    mobile=models.IntegerField(null=True, blank=True, default=None)
    cgpa=models.FloatField(null=True, blank=True, default=None)
    def __str__(self):
        return self.fname



    # document=models.FileField(upload_to='resume/',default='')
    

    
    
    
    

    