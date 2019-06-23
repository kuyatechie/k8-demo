from django.shortcuts import render

from django.http import HttpResponse

import socket

def index(request):
    return HttpResponse("Hello, world. I am your Kubernetes Pod Friend, {}. You're at the table index.".format(socket.gethostbyname(socket.gethostname())))
