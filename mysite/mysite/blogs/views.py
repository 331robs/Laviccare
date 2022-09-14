from re import template
from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
def donate(request):
    return render(request,'donate.html')

