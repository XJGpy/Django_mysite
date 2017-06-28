# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post

# Create your views here.

from django.http import HttpResponse

def index(request):
	#return HttpResponse("Welcome to my Blog!")
	post_list = Post.objects.all().order_by('-created_time')
	return render(request, 'blog/index.html', context={
			#'title': 'My Blog', 
			#'welcome': 'Welcome to my blog!!'
			'post_list': post_list
	})

