from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown
from datetime import datetime
from django.http import HttpResponse


class site:
    email = "3395538560@qq.com"
    twitter_username = None
    facebook_username = None
    linkedin_username = None
    github_username = "uu9"
    date = "2019"
    author = "Soranosro"
    title = "Soranosro"
    description = "In this altitude, we are at least not alone."


def index(request):
    PostList = Post.objects.order_by('-id')
    PostList = PostList[0:5]
    class page:
        background = "img/bg-index.jpg"
    context = {
        'PostList': PostList,
        'site': site,
        'page': page,
    }
    return render(request, 'home.html', context)


def about(request):
    class page:
        background = "img/bg-about.jpg"
        title = "About"
    context = {
        'site': site,
        'page': page,
    }
    return render(request, 'about.html', context)


def posts(request):
    PostList = Post.objects.order_by('-id')
    class pageINFO:
        background = "img/bg-post.jpg"
        title = "Posts"
        subtitle = ""
    paginator = Paginator(PostList, 5)  # 每页显示3篇文章
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
    # 如果page参数不是一个整数就返回第一页
        posts = paginator.page(1)
    except EmptyPage:
    # 如果页数超出总页数就返回最后一页
        posts = paginator.page(paginator.num_pages)
    context = {
        'PostList': posts,
        'site': site,
        'pageINFO': pageINFO,
        'page': page,
    }
    return render(request, 'posts.html', context)


def post_detail(request, year, month, day, id):
    post = get_object_or_404(Post, id=id)
    post.body = markdown.markdown(post.body, extensions=[
                          'markdown.extensions.extra',
                          'markdown.extensions.codehilite',
                          'markdown.extensions.toc',
                      ])
    class page:
        background = "img/bg-post.jpg"
        title = post.title
        description = "Post by " + str(post.author) + " on " + str(post.created_time)
    return render(request, 'page.html', {'content': post.body, 'page': page, 'site': site})


def post_detail_test(request, id):
    post = get_object_or_404(Post, id=id)
    post.body = markdown.markdown(post.body, extensions=[
                          'markdown.extensions.extra',
                          'markdown.extensions.codehilite',
                          'markdown.extensions.toc',
                      ])

    class page:
        background = "img/bg-post.jpg"
        title = post.title
        description = "Post by " + str(post.author) + " on " + str(post.created_time)
    return render(request, 'page.html', {'content': post.body, 'page': page, 'site': site})

# Create your views here.
