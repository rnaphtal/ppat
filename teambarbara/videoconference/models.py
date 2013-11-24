from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class UserProfile(models.Model):
    user= models.OneToOneField(User)
    #name = models.CharField(max_length=200)
    element_id = models.CharField(max_length=200)
    #user = models.OneToOneField(User)
    

    def __unicode__(self):
        return self.user.username


class Meeting (models.Model):
    name = models.CharField(max_length=200)
    participants = models.ManyToManyField(UserProfile)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
