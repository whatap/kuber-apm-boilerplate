from django.shortcuts import render
import os
import time
from django.http import HttpResponse
from movies.tasks import add, mul, xsum, task_iter
import time
import requests
# Create your views here.

def home(request):
    print("home")
    add.delay(9999,9999)
    return HttpResponse("home")

def sleep_test(request):
    print("sleep_test")
    add.delay(9999,9999)
    time.sleep(5)
    return HttpResponse("home")
def test(request):
    print("test")
    task_iter.delay(100000000)
    return HttpResponse("test")
