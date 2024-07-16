from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, NewsCreate, NewsUpdate, NewsDelete, ArticleCreate, ArticleUpdate, ArticleDelete


urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view()),

   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),

   path('article/create/', ArticleCreate.as_view(), name='article_create'),
   path('article/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
   path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete')
]