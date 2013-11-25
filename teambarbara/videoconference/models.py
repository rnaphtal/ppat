from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.


class UserProfile(models.Model):
    #user= models.OneToOneField(User)
    name = models.CharField(max_length=200)
    element_id = models.CharField(max_length=200)
    room_name = models.CharField(max_length=200)
    #user = models.OneToOneField(User)
    

    def __unicode__(self):
        return self.name


class Meeting (models.Model):
    name = models.CharField(max_length=200)
    participants = models.ManyToManyField(UserProfile)

    def __unicode__(self):
        return self.name

#User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class UserProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    room_name = forms.CharField(max_length=100)
    #meeting = models.ManyToManyField(Meeting)
    #authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

    def __unicode__(self):
        return self.name
