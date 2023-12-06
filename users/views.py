from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, 'form.html')
    elif request.method == "POST":
        return HttpResponse("post요청 들어옴")
    else:
        # 좋은 코드 X
        return HttpResponse("허용되지 않은 메소드입니다.")


from django.contrib.auth import authenticate, login as loginsession  # login as loginsession 이라는 별명을 줌!!

from django.contrib.auth import authenticate, login as loginsession  # login as loginsession 이라는 별명을 줌!!


def login(request):
    if request.method == "GET":  # GET 요청이 들어오면
        return render(request, 'login.html')
    elif request.method == "POST":  # POST의 경우
        username = request.POST.get('username')  # get은 7번줄의 GET과 다르다! 키 값이 username인 것을 가지고 와라!
        password = request.POST.get('password')
        # print(username, password, passwordcheck)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            loginsession(request, user)  # login 함수랑 똑같은 이름을 쓴게 2개라 임포트를 바꿀 때 as dlkfsjfdi 등등 별명 만들기라 생각하면된다.!
            return redirect('users:user')

        else:
            return HttpResponse("로그인 실패")


def user(request):
    print(request.user)  # 확인하는 방법 key 값
    return HttpResponse(request.user)