from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Post
# from .models import Event

# Create your views here.
# def my_blog(request):
#    return HttpResponse("Hello, Blog!")

class PostList(generic.ListView):


    queryset = Post.objects.filter(status=1)
    # template_name = "post/index.html"
    template_name = "blog/index.html"
    # model = Event
    # template_name = "index.html"
    paginate_by = 12


# def event_detail(request, event_id):


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post} )