from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

messages = {
    'index':'<h1>Salom bu index file</h1>',
    'najot':'<h1>Najot Talimda</h1>',
    'murodjon':'<h1>Murodjon Tokhirov 1997</h1>',
    'akmal':'<h1>Akmal Ulanov 1988</h1>',
    'islom':'<h1>Islom Galiyev 1999</h1>',
    'sherzod':'<h1>Sherzod Gayratov 2008</h1>',
    'dilmuhammad':'<h1>Dilmuhammad Abdukodirov 2006</h1>'
}

def index(request,topic):
    try:
        return HttpResponse(messages[topic])
    except:
        return HttpResponseNotFound('<center><h1>This page does not exists</h1></center>')