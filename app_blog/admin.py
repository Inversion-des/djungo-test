from django.contrib import admin
from django.shortcuts import get_object_or_404

from .models import Article, ArticleImage, Category, Comment


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category', 'slug')
	prepopulated_fields = {'slug': ('category',)}
	fieldsets = (
		('', {
			'fields': ('category', 'slug'),
		}),
	)

admin.site.register(Category, CategoryAdmin)


class ArticleImageInline(admin.TabularInline):
	model = ArticleImage
	extra = 0
	fieldsets = (
		('', {
			'fields': ('title', 'image'),
		}),
	)


class ArticleAdmin(admin.ModelAdmin):
	# columns to display for the list of articles in the admin panel
	list_display = ('title', 'pub_date', 'slug', 'main_page', 'category')
	fieldsets = (
		('', {
			'fields': ('pub_date', 'title', 'description', 'category', 'main_page'),
		}),
		('Додатково', {
			'fields': ('slug',),
		}),
	)
	prepopulated_fields = {'slug': ('title',)}
	inlines = [ArticleImageInline]

	def delete_file(self, pk, request):
		'''Delete an image.'''
		obj = get_object_or_404(ArticleImage, pk=pk)
		return obj.delete()

admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'body', 'created_on', 'article')
	fieldsets = (
		('', {
			'fields': ('name', 'email', 'body', 'article'),
		}),
	)

admin.site.register(Comment, CommentAdmin)