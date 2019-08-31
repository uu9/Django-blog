import json
import requests
import django
from lxml import etree
from . import getordefault


def searchrank(request):
    acid = getordefault(request, "id", None)
    r = requests.get('http://dota.ali213.net/searchResult/', {"account_id": acid})
    selector = etree.HTML(r.text)
    rank = selector.xpath('/html/head/script[5]/text()')
    raw_json = rank[0][11:-1]
    jsonDat = json.loads(raw_json)
    if jsonDat.get("error") is not None:
        r = requests.get('http://dota.ali213.net/getAccoundId', {"nickname": acid})
        acid = r.text
        r = requests.get('http://dota.ali213.net/searchResult/', {"account_id": acid})
        selector = etree.HTML(r.text)
        rank = selector.xpath('/html/head/script[5]/text()')
        raw_json = rank[0][11:-1]
        jsonDat = json.loads(raw_json)
    try:
#        score = jsonDat["profile"]["single_score"]
#        rd = {"id": acid, "info": score}
        return jsonDat
    except KeyError:
        info = "未查询到数据"
        rd = {"id": acid, "info": info}
        return rd
