from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')
def musics(request):
    return render(request, 'frontend/musics.html')
def member(request):
    return render(request, 'frontend/member.html')
def about(request):
    return render(request, 'frontend/about.html')
def contact(request):
    return render(request, 'frontend/contact.html')
def ryujin(request):
    return render(request, 'frontend/ryujin.html')
def chaeryeong(request):
    return render(request, 'frontend/chaeryeong.html')
def yuna(request):
    return render(request, 'frontend/yuna.html')
def lia(request):
    return render(request, 'frontend/lia.html')
def yeji(request):
    return render(request, 'frontend/yeji.html')
def c1(request):
    return render(request, 'image/c1.jpg')

