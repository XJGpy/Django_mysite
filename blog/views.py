# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
import markdown
from django.http import HttpResponse

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

