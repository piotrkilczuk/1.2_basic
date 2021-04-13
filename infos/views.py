from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def homepage(request):
      return render(
            request=request,
            template_name="infos/main.html",
            context={"Title": "Homepage"}
      )

def about_me(request):
      return render(
            request=request,
            template_name="infos/me.html",
            context={"Title": "About me"}
      )

def contact(request):
      return render(
            request=request,
            template_name="infos/contact.html",
            context={"Title": "Contact"}
      )