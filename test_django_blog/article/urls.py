from django.urls import path
from django.views import View
from test_django_blog.article import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles'),
    path('<int:id>/', views.ArticleView.as_view(), name='article'),
    path('create/', views.ArticleFormCreateView.as_view(), name='articles_create'),
    path('comment/', views.ArticleCommentFormView.as_view(), name='comment_create'),
    path('<int:id>/edit/', views.ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/delete/', views.ArticleFormDestroyView.as_view(), name='articles_destroy'),
]