from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def map(request):
	context = { }
	return render(request, "map.html", context)