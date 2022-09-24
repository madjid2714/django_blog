from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from posts.models import BlogPost

from django.urls import reverse_lazy


class BlogHome(ListView):
	model = BlogPost
	context_object_name = "posts"

	def get_queryset(self):
		queryset = super().get_queryset()
		if self.request.user.is_authenticated:
			return queryset
		return queryset.filter(published=True)


class BlogPostCreate(CreateView):
	model = BlogPost
	template_name = "posts/blogpost_create.html"
	fields = ['title', 'content',]



class BlogPostUpdate(UpdateView):
	model = BlogPost
	template_name = "posts/blogpost_edit.html"
	fields = ['title', 'content', 'published']

class BlogPostDelete(DeleteView):
	model = BlogPost
	# template_name = "posts/blogpost_delete.html"
	context_object_name = "post"
	success_url = reverse_lazy("posts:home")

class BlogPostDetail(DetailView):
	model = BlogPost
	context_object_name = "post"
