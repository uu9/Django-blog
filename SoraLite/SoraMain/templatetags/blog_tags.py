from django import template
from ..models import Post
from datetime import datetime


register = template.Library()
@register.simple_tag
def total_posts():
    return Post.objects.all().count()

@register.simple_tag
def time_count():
    q = Post.objects.all()
    nowIs = datetime.now()
    pastIs = datetime.strptime(str(q[0].created_time).split('+')[0], "%Y-%m-%d %H:%M:%S")
    timeStartPoint = nowIs - pastIs
    return int(timeStartPoint.days)
