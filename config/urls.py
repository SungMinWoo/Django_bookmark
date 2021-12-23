"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index, welcome, template_test

urlpatterns = [
    path('bookmark/', include('bookmark.urls')), # 1차 -> 2차 -> 3차
    path('admin/', admin.site.urls),
    path('welcome/wel', welcome),
    path('test/', template_test),
    path('', index),

    # path(주소, 뷰, 주소의 별명)
    # 왠만하면 메인 페이지 사이에 url 추가
]
