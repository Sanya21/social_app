from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
import requests
from . import vk_social
# Create your views here.


def index(request):
    if 'testflask' not in request.COOKIES:
        return render(request, 'home.html')
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/login")


def login(request):
    try:
        link = "https://oauth.vk.com/authorize?client_id=7429099&redirect_uri=http://127.0.0.1:8000/final&display=page&scope=friends&response_type=code&v=5.103"
        #link = "https://oauth.vk.com/authorize?client_id=7429099&scope=friends,offline&redirect_uri=http://www.vkauth.website/vk_app/final/&response_type=code"
        r = requests.get(url=link)
        return HttpResponseRedirect("https://oauth.vk.com/authorize?client_id=7429099&redirect_uri=http://127.0.0.1:8000/final&display=page&scope=friends&response_type=code&v=5.103")
            #HttpResponseRedirect("https://oauth.vk.com/authorize?client_id=7429099&scope=friends,offline&redirect_uri=http://www.vkauth.website/vk_app/final/&response_type=code")
    except Exception as e:
        response = "<h1 style='color:blue'>Сервер ВКонтакте временно недоступен. Повторите попытку позже. </h1>"
        return HttpResponse(response)


def final(request):
    current_url = request.build_absolute_uri()
    code = current_url[34:]

    report = vk_social.auth(code)
    if 'testflask' not in request.COOKIES:
        response = HttpResponse(report)
        response.set_cookie('testflask', 'VK_auth', max_age=60*60*24*365*2)
    else:
        response = HttpResponse(report)
    return response
