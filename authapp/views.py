from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text = """<h1>Auth App</h1>"""
    return HttpResponse(text)