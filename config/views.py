from django.http import HttpResponse
from django.shortcuts import render

def index(request): # 함수형 뷰
    # 어떤 계산이나, 데이터베이스 조회, 수정, 등록
    # 응답 메세지를 만들어서 반환.
    html = "<html><body>Hello</body></html>"
    # 추후 html 변수를 대신해서 템플릿 넣으면됨
    return HttpResponse(html)


def welcome(request):
    html = '<html><body>Welcome to django</body></html>'
    return HttpResponse(html)


def template_test(request):
    # 기본 템플릿 폴더
    # 1. admin 앱
    # 2. 각 앱의 폴더에 있는 templates 폴더
    # 3. 내가 설정한 폴더
    return render(request, 'templates.html')