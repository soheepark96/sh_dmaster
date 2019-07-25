from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Board

# Create your views here.

# def board(request):
#     return render(request, 'board/board.html')

def board_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        password = request.POST.get('pwd')

        if request.session.get('user') == False :
            return render(request, 'main/home.html')
        
        user = request.session['user']
        # else 를 따로 안 써줘도 됨 , if 에서 return 으로 보내므로 else 시 작동 안함
        board = Board (
            title = title,
            author = author,
            content = content,
            password = password,
            User_info = user
        )
        board.save()
        boards = Board.objects.all()
        context = {'boards' :  boards}
        return render(request, 'board/board_view.html', context)
    else:
        return render(request, 'board/board.html')

def board_view(request):
    if Board.objects.all() != None :
        boards = Board.objects.all()
        context = {'boards' : boards }
        return render(request, 'board/board_view.html', context)
    else :
        return render(request, 'board/board_view.html')

def board(request, pk):
    board = Board.objects.get(pk=pk)
    # get 은 하나의 파일? 가져오는것..
    context = {'board' : board}
    return render(request, 'board/board_detail.html', context)

def board_update(request, pk):
    # redirect 는 view 와 view 를 연결 , 함수 재사용
    # pk 값은 고유번호
    if request.POST.get('pwd') == Board.objects.get(pk=pk).password :
        if request.POST.get("title") and request.POST.get("author") and reqeust.POST.get("content") :
            board = Board.objects.get(pk=pk)
            board.title = request.POST.get("title")
            board.author = request.POST.ger("author")
            board.content = request.POST.ght("content")
            board.save()
            return redirect('board', pk=board.id)
        else : 
        # 처음 접근했을 때의 화면, create html 을 재사용 
            board = Board.objects.get(pk=pk)
            context = {"board" : board}
            return render(request, "board/board.html", context)
    else :
        return redirect("board", pk=pk)

def board_delete(request, pk):
    board = Board.objects.get(pk=pk)
    if request.POST.get("pwd") !=board.password :
        return redirect(reverse("board"), pk=pk)
    board.delete()
    return redirect(reverse("board_view"))



