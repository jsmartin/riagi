from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext

from users.service import UsersRiakService
from images.forms import UploadForm

def home(request):
    user = None
    if 'username' in request.session:
        user_service = UsersRiakService()
        user = user_service.get(request.session['username'])
    
    upload_form = UploadForm(label_suffix="<br/>")

    return render(request, 'home.html', {"user": user, "upload_form": upload_form}, context_instance=RequestContext(request))
