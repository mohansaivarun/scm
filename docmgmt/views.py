from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sample(res):
    return HttpResponse(
        "<html><h1>This is Document Management</h1></html>"
    )