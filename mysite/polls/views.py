from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    detail = {"Name": "PRASHANT", "Age":21, "Address": "chabahil"}
    context ={'detail':detail}
    return render(request,"home.html",context)

def detail(request):
    return HttpResponse("You are in detail page")

# Create your views here.
