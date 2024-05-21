from django.views.generic import ListView, DateDetailView
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from .models import Article, Category, Comment
from .forms import CommentForm

class HomePageView(ListView):
	model = Article
	template_name = 'index.html'
	context_object_name = 'categories'

	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		context['articles'] = Article.objects.filter(main_page=True)[:1]
		context['other_articles'] = Article.objects.filter(main_page=False)[:3]
		return context

	def get_queryset(self, *args, **kwargs):
		categories = Category.objects.all()
		return categories


class ArticleDetail(DateDetailView):
	model = Article
	template_name = 'article_detail.html'
	context_object_name = 'item'
	date_field = 'pub_date'
	query_pk_and_slug = True
	month_format = '%m'
	allow_future = True

	def get_context_data(self, *args, **kwargs):
		context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
		context['comments'] = Comment.objects.filter(article=self.object)
		context['comment_form'] = CommentForm()
		try:
			context['images'] = context['item'].images.all()
		except:
			pass
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		context = self.get_context_data(object=self.object)
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.article = self.object
			new_comment.save()
			return redirect(self.object.get_absolute_url())
		else:
			context['comment_form'] = comment_form
			return self.render_to_response(context)


class ArticleList(ListView):
	model = Article
	template_name = 'articles_list.html'
	context_object_name = 'items'

	def get_context_data(self, *args, **kwargs):
		context = super(ArticleList, self).get_context_data(*args, **kwargs)
		try:
			context['category'] = Category.objects.get(slug=self.kwargs.get('slug'))
		except Exception:
			context['category'] = None

		return context

	def get_queryset(self, *args, **kwargs):
		articles = Article.objects.all()
		return articles


class ArticleCategoryList(ArticleList):

	def get_queryset(self, *args, **kwargs):
		articles = Article.objects.filter(
			category__slug__in=[self.kwargs['slug']]
		).distinct()
		return articles
