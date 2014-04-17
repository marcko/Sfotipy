from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Track 
def track_view(request, title):

	track = get_object_or_404(Track, title = title)
	#return HttpResponse('ok')
	return render(request, 'track.html',{'track' :track})