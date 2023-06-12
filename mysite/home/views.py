from django.shortcuts import render
from django.http import HttpResponse

def homepageMsg(request):
    return render(request,'index.html')
# Create your views here.
def about(request):
    return HttpResponse("welcome to about page")
def contact(request):
    return HttpResponse("welcome to contact page")