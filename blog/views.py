from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('<h1>Hello World</h1>')


def post_list(request):
	return render(request, 'post_list.html')