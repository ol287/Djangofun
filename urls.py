from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  # Home page showing list of posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Detail view of a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Update an existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post
    path('admin/', admin.site.urls),
    path('post/<int:pk>/like/', views.like_post, name='like-post'),
    path('', include('blog.urls')),
    path('', include('users.urls')),
]
