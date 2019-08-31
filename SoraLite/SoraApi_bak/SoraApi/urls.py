from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('docs/<slug:doc>', views.api, name='api'),
    path('api/<slug:name>', views.use, name='use'),
]