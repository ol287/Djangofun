from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# View to list all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # Specify the template to use
    context_object_name = 'posts'
    ordering = ['-date_posted']  # Order posts by date (newest first)

# View to display details of a single post
class PostDetailView(DetailView):
    model = Post

# View to create a new post (login required)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # Override the form_valid method to set the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# View to update an existing post (login and authorization required)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # Override the form_valid method to set the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Method to check if the current user is the author of the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# View to delete an existing post (login and authorization required)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # Redirect to home page after deletion

    # Method to check if the current user is the author of the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
