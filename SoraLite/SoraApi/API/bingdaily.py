import requests
from . import getordefault
import django


def bingdaily(request):
    index = getordefault(request, "index", 0)
    n = getordefault(request, "n", 1)
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
                'cookie': "ENSEARCH=TIPBUBBLE=1&BENVER=1"}
    r = requests.get("https://cn.bing.com/HPImageArchive.aspx?format=js&pid=hp&quiz=1&og=1" +
                     ("&idx={}&n={}".format(index, n)), headers=headers)
    # https://cn.bing.com/HPImageArchive.aspx?format=js&pid=hp&quiz=1&og=1
    rd = r.json()
    rd.pop("tooltips")
    return rd