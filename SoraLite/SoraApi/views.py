from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse, Http404
from .API import *

def index(request):
    filenames = os.listdir(os.path.join(settings.BASE_DIR, "SoraApi/templates/ApiDetail"))
    namelist = []
    for i in filenames:
        if i.endswith(".html"):
            namelist.append(os.path.splitext(i)[0])
    yan = yiyan.yiyan()
    content = {"namelist": namelist, "part": "layouts/components/Intros.html",
               "words": yan['hitokoto'], "from": yan["from"]}
    return render(request, 'index.html', content)

def api(request, doc):
    filenames = os.listdir(os.path.join(settings.BASE_DIR, "SoraApi/templates/ApiDetail"))
    namelist = []
    for i in filenames:
        if i.endswith(".html"):
            namelist.append(os.path.splitext(i)[0])
    yan = yiyan.yiyan()
    if doc in namelist:
        content = {"namelist": namelist, "part": "ApiDetail/"+doc+".html",
                   "words": yan['hitokoto'], "from": yan['from']}
        return render(request, 'index.html', content)
    else:
        raise Http404()

def func(x, request):
    filenames = os.listdir(os.path.join(settings.BASE_DIR, "SoraApi/API"))
    namelist = []
    for i in filenames:
        if i.endswith(".py"):
            namelist.append(os.path.splitext(i)[0])
    if x in namelist:
        res = eval("{}.{}({})".format(x, x, "request"))
    return res

def use(request, name):
    name = str(name).lower()
    filenames = os.listdir(os.path.join(settings.BASE_DIR, "SoraApi/API"))
    namelist = []
    for i in filenames:
        if i.endswith(".py"):
            namelist.append(os.path.splitext(i)[0])
    argvs = "request.GET"
    if name in namelist:
        result = func(name, request)
        return JsonResponse(result)
    else:
        raise Http404()
# Create your views here.
