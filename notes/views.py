from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


# 메모 목록을 띄우는 코드
def note_list(request):
    notes = Note.objects.all()
    # render: html 파일과 연결 시도!
    return render(request, "notes/note_list.html", {"notes": notes})


# 메모장 생성
def note_create(request):
    # 사용자 폼을 post형식으로 받아야함.
    # 사용자가 메모장을 생성했을 때 POST로 받아야함.
    # 사용자 생성한 메모장이 POST 일 때 폼이 정상적으로 작동한다.
    if request.method == "POST":
        form = NoteForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            form.save()  # 데이터베이스 저장
            # fedirect('url'): url 주소로 이동
            return redirect("note_list")  # 목록으로 이동
    else:  # 처음 들어왔을 떄
        form = NoteForm()
        return render(request, "notes/note_create.html", {"form": form})


# 메모장 상세보기
# pk: 리스트 하나하나에 부여된 고유 숫자
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


# 메모장 수정하기
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    # 메모장을 사용자가 수정을 완료햇을 때
    if request.method == "POST":
        # 수정
        form = NoteForm(request.POST, instance=note)
        # 유효성 검사
        if form.is_valid():
            form.save()  # 데이터베이스 저장
            # fedirect('url'): url 주소로 이동
            return redirect("note_detail", pk=note.pk)
    else:
        form = NoteForm(instance=note)
        return render(request, "notes/note_create.html", {"form": form})
