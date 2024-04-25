from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.
# def my_blog(request):
#    return HttpResponse("Hello, Blog!")

class PostList(generic.ListView):
    queryset = Post.objects.filter()
    # template_name = "post/index.html"
    template_name = "blog/index.html"
    paginate_by = 6