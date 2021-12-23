from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from .models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url'] # 수정할 내용
    success_url = reverse_lazy('list') # 이동할 url 정보
    template_name_suffix = '_create'
    # template_name_suffix은 없으면 모델명_폼 형태를 불러옴


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    # template_name_suffix은 없으면 모델명_폼 형태를 불러옴


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
    # template_name_suffix = 'confirm_delete'
    # class안에는 무조건 reverse_lazy를 사용한다.
