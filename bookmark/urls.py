from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView

urlpatterns = [
    # http://127.0.0.1/bookmark/ 이후의 url를 정의하는 것
    path("", BookmarkListView.as_view(), name='list'), # class형 뷰일때 as_vuew()를 넣어야하고 함수형 view는 안넣어도됨
    path("add/", BookmarkCreateView.as_view(), name='add'), # name 뒤는 나중에 template에서 불러오는것
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'), # pk 글 번호를 링크로 연결해주는 것
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]
