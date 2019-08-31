from ..models import Baigeng
import random


def baigeng(request):
    if request.method == "GET":
        return get(request)
    elif request.method == "POST":
        return post(request)
    else:
        return {"info": "本网站禁止非法请求!!!"}


def post(request):
    name = request.POST.get("name", None)
    content = request.POST.get("content", None)
    creator = request.POST.get("creator", None)
    contact_creator = request.POST.get("contact_creator", "")
    related_person = request.POST.get("related_person", None)
    tp = request.POST.get("type", "")
    source = request.POST.get("source", "")
    rank = request.POST.get("rank", None)
    if not rank.isdigit():
        rank = 0
    else:
        rank = int(rank)
    print(name, content, creator, related_person)
    if not (name or content or creator or related_person):
        return {"status": "error, name, content, creator, related_person should not be empty"}
    if name:
        a = Baigeng.objects.filter(name__contains=name)
        if len(a) != 0:
            return {"status": "error, maybe something similar already exists"}
    if not rank:
        rank_num = 1
    else:
        rank_num = 0
    try:
        print("try create data")
        Baigeng.objects.create(name=name, content=content, use=False,
                                creator=creator, contact_creator=contact_creator,
                                related_person=related_person, type=tp,
                                source=source, rank=rank, rank_num=rank_num)
    except BaseException:
        return {"status": "error, check data"}
    return {"status": "ok"}


def get(request):
    name = request.GET.get("name", None)
    rp = request.GET.get("rp", None)
    content = request.GET.get("content", None)
    source = request.GET.get("source", None)
    print(name, rp, content, source)
    if name or rp or content or source:
        a = Baigeng.objects.all()
        if name:
            a = a.filter(name__contains=name)
        if rp:
            a = a.filter(rp__contains=rp)
        if content:
            a = a.filter(content__contains=content)
        if source:
            a = a.filter(source__contains=source)

        if len(a) == 0:
            return {"status": "not found"}
        elif len(a) == 1:
            return getcontent(a[0])
    else:
        r = Baigeng.objects.all()
        if len(r) <1:
            return {"status": "error, no data"}
        else:
            n = random.randint(0, len(r)-1)		
            return getcontent(r[n])


def getcontent(r):
    rd = {"id": r.id, "name": r.name, "content": r.content,
          "modified_time": r.modified_time, "created_time": r.created_time,
          "creator": r.creator, "related_person": r.related_person,
          "type": r.type, "source": r.source, "rank": r.rank,
          "rank_num": r.rank_num}
    return rd
