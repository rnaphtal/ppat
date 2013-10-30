# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    #return HttpResponse("Hello, world. You're at the video conference app index.")
    template = loader.get_template('videoconference/index.html')
    context = RequestContext(request, {
        
    })
    return HttpResponse(template.render(context))

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)
