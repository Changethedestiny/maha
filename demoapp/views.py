from django.shortcuts import render

# Create your views here.
from django. http import HttpResponse

def home(request):
    return HttpResponse("this my first app in home app")
def demo(request):
    return HttpResponse("thanks for watching")
