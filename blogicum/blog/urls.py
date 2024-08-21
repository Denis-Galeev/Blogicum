from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [

    path(  # FBV index
        '',
        views.index,
        name='index'
    ),
    path(  # FBV post_detail
        'posts/<int:post_id>/',
        views.post_detail,
        name='post_detail'
    ),
    path(  # FBV category_posts
        'category/<slug:category_slug>/',
        views.category_posts,
        name='category_posts'
    ),
    path(  # FBV create_post
        'posts/create/',
        views.create_post,
        name='create_post'
    ),
    path(  # FBV edit_post
        'posts/<int:post_id>/edit/',
        views.edit_post,
        name='edit_post'
    ),
    path(  # FBV delete_post
        'posts/<int:post_id>/delete/',
        views.delete_post,
        name='delete_post'
    ),
    path(  # FBV profile
        'profile/<str:username>/',
        views.profile,
        name='profile'
    ),
    path(  # FBV edit_profile
        'edit_profile/',
        views.edit_profile,
        name='edit_profile'
    ),
    path(  # FBV views.add_comment
        'posts/<int:post_id>/comment/',
        views.add_comment,
        name='add_comment'
    ),
    path(  # FBV views.edit_comment
        'posts/<int:post_id>/edit_comment/<int:comment_id>/',
        views.edit_comment,
        name='edit_comment'
    ),
    path(  # FBV views.delete_comment
        'posts/<int:post_id>/delete_comment/<int:comment_id>/',
        views.delete_comment,
        name='delete_comment'
    )
]
