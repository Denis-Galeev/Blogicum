from django.db.models import Count, Manager, QuerySet  # type: ignore
from django.utils.timezone import now  # type: ignore


class PostQuerySet(QuerySet):

    def with_related_data(self):
        return self.select_related(
            'author',
            'category',
            'location'
        )

    def published(self):
        return self.filter(
            is_published=True,
            pub_date__lt=now(),
            category__is_published=True
        )

    def comment_count(self):
        return self.annotate(
            comment_count=Count("comments")
        ).order_by('-pub_date')

    def by_author(self, author):
        return self.filter(author=author)

    def by_category(self, category):
        return self.filter(category=category)


class PostManager(Manager):

    def get_queryset(self):
        return (
            PostQuerySet(self.model)
            .with_related_data()
        )

    def get_pub(self):
        return (
            self.get_queryset()
            .published()
        )

    def get_for_index(self):
        return (
            self.get_queryset()
            .published()
            .comment_count()
        )

    def get_for_category(self, category):
        return (
            self.get_queryset()
            .published()
            .by_category(category)
            .comment_count()
        )

    def get_for_profile(self, author):
        return (
            self.get_queryset()
            .published()
            .by_author(author)
            .comment_count()
        )

    def get_for_profile_auth(self, author):
        return (
            self.get_queryset()
            .by_author(author)
            .comment_count()
        )
