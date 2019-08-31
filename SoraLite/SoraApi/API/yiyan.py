import requests
from . import getordefault


def yiyan(request=None):
    try:
        tp = getordefault(request, "type", None)
    except AttributeError:
        tp = None
    if tp is not None:
        r = requests.get("https://v1.hitokoto.cn/", {"c": tp})
        rd = r.json()
        return rd
    else:
        r = requests.get("https://v1.hitokoto.cn/")
        rd = r.json()
        return rd