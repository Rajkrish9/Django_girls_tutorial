from django.shortcuts import render 
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

# Create your views here.
from django.shortcuts import render

# Create your views here.
def post_list(request):

    #posts = Post.objects.filter 

    return render(request, 'blog/post_list.html', {})

    #blog/post_list.html