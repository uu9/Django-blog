from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from SoraMain.sitemaps import PostSitemap
from django.contrib import admin


sitemaps = {'posts': PostSitemap,}

urlpatterns = [
    path('', views.index, name='index'),
	path('admin/', admin.site.urls),
    path('posts/', views.posts, name='posts'),
    path('about/', views.about, name='about'),
    path('posts/<int:id>/', views.post_detail_test, name='post_detail_test'),
    path('<int:year>/<int:month>/<int:day>/<int:id>/', views.post_detail, name='post_detail'),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]