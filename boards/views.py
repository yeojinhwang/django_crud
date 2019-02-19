# 1. 파이썬 표준 라이브러리 ex) os, random
# 2. Core Django : 장고 프레임워크에 있는 것
from django.shortcuts import render, HttpResponse, redirect
# 3. 3rd party library : django_extensions 등
# 4. 장고 프로젝트 App
from .models import Board # 명시적 상대 import vs 암묵적 상대 import(from models import Board)

# Create your views here.
def index(request):
    boards = Board.objects.order_by('-id')
    return render(request, 'boards/index.html', {'boards': boards})
    
def new(request):
    return render(request, 'boards/new.html')
    
def create(request):
    board = Board()
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    # return render(request, 'boards/create.html', {'board': board})
    return redirect(f'/boards/detail/{board.id}')
    
def detail(request, pk):
    board = Board.objects.get(id=pk)
    return render(request, 'boards/detail.html', {'board': board})
    
def delete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    response = redirect('/boards/')
    return response
    
def edit(request, pk):
    board = Board.objects.get(id=pk)
    return render(request, 'boards/edit.html', {'board': board})
    
def update(request, pk):
    board = Board.objects.get(id=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect(f'/boards/detail/{board.id}')