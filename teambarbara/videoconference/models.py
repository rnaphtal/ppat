from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
import django.dispatch

# Create your models here.


class UserProfile(models.Model):
    #user= models.OneToOneField(User)
    name = models.CharField(max_length=200, unique=True)
    element_id = models.CharField(max_length=200)
    room_name = models.CharField(max_length=200)
    #user = models.OneToOneField(User)
    

    def __unicode__(self):
        return self.name

    def enter_room (self, room):
        print "sending"
        user_entered.send(sender=UserProfile, room=room, user = self)


class Meeting (models.Model):
    name = models.CharField(max_length=200)
    participants = models.ManyToManyField(UserProfile)

    def __unicode__(self):
        return self.name

#User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=['name','room_name']
    #name = forms.CharField(max_length=200)
    #room_name = forms.CharField(max_length=100)
    #meeting = models.ManyToManyField(Meeting)
    #authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

    def __unicode__(self):
        return self.name

user_entered = django.dispatch.Signal(providing_args=["data"])



