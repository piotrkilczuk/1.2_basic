from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def homepage(request):
      c = {"Title": "Strona główna"}
      return render(
            request=request,
            template_name="infos/main.html",
            context=c
      )

def about_me(request):
      return render(
            request=request,
            template_name="infos/me.html"
      )

def contact(request):
      return render(
            request=request,
            template_name="infos/contact.html"
      )