from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app_blog import views
from .views import (HomePageView, ArticleDetail, ArticleList, ArticleCategoryList)

urlpatterns = [
	path('', views.HomePageView.as_view()),
	path(r'articles', ArticleList.as_view(), name='articles-list'),
	path(r'articles/category/<slug>', ArticleCategoryList.as_view(), name='articles-category-list'),
	path(r'articles/<year>/<month>/<day>/<slug>', ArticleDetail.as_view(), name='news-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
