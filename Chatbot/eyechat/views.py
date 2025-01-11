from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'eyechat/index.html/')

def specific(request):
    return HttpResponse('number')

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)