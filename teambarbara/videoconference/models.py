from django.db import models

# Create your models here.

class UserProfile(models.Model):
    question = models.CharField(max_length=200)
    #user = models.OneToOneField(User)
    

    #def __unicode__(self):
#        return self.user.username

