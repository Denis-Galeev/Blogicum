from django.contrib.admin import ModelAdmin, site
from django.contrib.admin.decorators import register
from django.contrib.auth.models import Group

from blog.models import Category, Comment, Location, Post


@register(Location)
class LocationAdmin(ModelAdmin):
    """
    Административная панель для модели Location.

    Атрибуты:
    - list_display: отображаемые поля в списке.
    - list_editable: поля, которые можно редактировать прямо в списке.
    - search_fields: поля, по которым можно выполнять поиск.
    - list_filter: фильтры для списка местоположений.
    - list_display_links: поля-ссылки, по которым можно перейти
    к редактированию записи о локации.
    """

    list_display = ('name', 'is_published', 'created_at',)
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('name', 'is_published', 'created_at',)
    list_display_links = ('name',)


@register(Post)
class PostAdmin(ModelAdmin):
    """
    Административная панель для модели Post.

    Атрибуты:
    - list_display: отображаемые поля в списке постов.
    - list_editable: поля, которые можно редактировать прямо в списке.
    - search_fields: поля, по которым можно выполнять поиск.
    - list_filter: фильтры для списка постов.
    - list_display_links: поля-ссылки по которым можно перейти
    к редактированию поста.
    """

    list_display = (
        'title',
        'author',
        'category',
        'location',
        'is_published',
        'created_at'
    )
    list_editable = ('is_published', 'location', 'category',)
    search_fields = ('title', 'text', )
    list_filter = ('category', 'is_published', 'location', 'author',)
    list_display_links = ('title',)


@register(Category)
class CategoryAdmin(ModelAdmin):
    """
    Административная панель для модели Category.

    Атрибуты:
    - list_display: отображаемые поля в списке категорий.
    - list_editable: поля, которые можно редактировать прямо в списке.
    - search_fields: поля, по которым можно выполнять поиск.
    - list_filter: фильтры для списка категорий.
    - list_display_links: поля-ссылки, по которым можно перейти
    к редактированию записи о категории.
    """

    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at'
    )
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'slug',)
    list_filter = ('title', 'is_published', 'created_at',)
    list_display_links = ('title', 'slug')


@register(Comment)
class CommentAdmin(ModelAdmin):
    """
    Административная панель для модели Comment.

    Атрибуты:
    - list_display: отображаемые поля в списке комментариев.
    - list_editable: поля, которые можно редактировать прямо в списке.
    - search_fields: поля, по которым можно выполнять поиск.
    - list_filter: фильтры для списка комментариев.
    """

    list_display = (
        'text',
        'post',
        'author',
        'is_published',
        'created_at',
    )
    list_editable = ('is_published',)
    search_fields = ('text',)
    list_filter = ('post', 'is_published', 'created_at',)


site.empty_value_display = '-- Не задано --'
site.unregister(Group)
