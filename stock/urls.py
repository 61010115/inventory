from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('chaeryeong',views.chaeryeong, name='chaeryeong'),
    path('lia',views.lia, name='lia'),
    path('ryujin',views.ryujin, name='ryujin'),    
    path('yeji',views.yeji, name='yeji'),
    path('yuna',views.yuna, name='yuna'),
    path('member',views.member, name='member'),
    path('musics',views.musics, name='musics'),
]