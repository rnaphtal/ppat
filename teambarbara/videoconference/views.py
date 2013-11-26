# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, get_object_or_404
from models import *

def index(request):
    #return HttpResponse("Hello, world. You're at the video conference app index.")
    template = loader.get_template('videoconference/index.html')
    context = RequestContext(request, {
        
    })
    return HttpResponse(template.render(context))

def welcome (request):
    template = loader.get_template('videoconference/welcome.html')
    context = RequestContext(request, {
        
    })
    return HttpResponse(template.render(context))

def enterRoom(request, roomName, userProfile):
    allMeetings = Meeting.objects.all()
    meeting=-1
    for m in allMeetings:
        if m.name == roomName:
            meeting=m
    #print "MEETING:", meeting, meeting.participants.all()
    if meeting!=-1:
        meeting.participants.add(userProfile)
        meeting.save()
        otherUsers=meeting.participants.all()
        userProfile.enter_room (meeting)
        #Add callback for changed participants
        #@receiver(user_entered)
        def user_entered_callback(sender, **kwargs):
            kwargs.get("user")
            print("Entered callback")
        m2m_changed.connect(user_entered_callback)
        print "Callback created", user_entered_callback
    else:
        print "No meeting exists"
        otherUsers=[]
    print otherUsers
    
    
    #Need to add correct database queries to get this
    
    template = loader.get_template('videoconference/index.html')
    context = RequestContext(request, {
        'room_name' : roomName,
        'username' : userProfile.name,
        'others' : otherUsers
    })
    return HttpResponse(template.render(context))



def login(request, roomName):
    template = loader.get_template('login.html')
    context = RequestContext(request, {
        'room_name' : roomName,
    })
    return HttpResponse(template.render(context))

def create_user(request):
    if request.method == 'POST':
        
        user_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('name')
            roomName = user_form.cleaned_data.get('room_name')
            element_id=1
            user = UserProfile(name=username,
                                element_id=element_id, room_name = roomName)
            
            user.save()
            return enterRoom(request, roomName, user)

    return HttpResponse(user_form.cleaned_data)
    return enterRoom(request, "test")
