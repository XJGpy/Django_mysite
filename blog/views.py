# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
import markdown
from django.http import HttpResponse
from .models import Post, Category

def index(request):
	#return HttpResponse("Welcome to my Blog!")
	post_list = Post.objects.all().order_by('-created_time')
	return render(request, 'blog/index.html', context={
			#'title': 'My Blog', 
			#'welcome': 'Welcome to my blog!!'
			'post_list': post_list
	})

def detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.body = markdown.markdown(post.body,
				      extensions=[
				      		'markdown.extensions.extra',
                                                'markdown.extensions.codehilite', 
                                                'markdown.extensions.toc',
                                                ])
	return render(request, 'blog/detail.html', context={'post':post})

def archives(request, year,month):
	post_list = Post.objects.filter(created_time__year=year,
					created_time__month=month
					).order_by('-created_time')
	return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
	cate = get_object_or_404(Category, pk=pk)
	post_list = Post.objects.filter(category=cate).order_by('-created_time')
	return render(request, 'blog/index.html', context={'post_list':post_list})

