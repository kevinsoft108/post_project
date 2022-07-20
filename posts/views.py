from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Post, Topics


# Create your views here.
class PostListView(LoginRequiredMixin, generic.ListView):
    template_name = 'posts/index.html'
    paginate_by = 6
    model = Post

    def get_queryset(self, **kwargs):
        topic_id = 1
        posts = Post.objects.filter(topic_id=topic_id)
        return posts

    def get_context_data(self, **kwargs):
        blogs_list = super().get_context_data(**kwargs)
        topic = Topics.objects.all()
        title = 1
        context = {
            'blogs_list': blogs_list,
            'posts': blogs_list['object_list'],
            'title': title,
            'topics': topic
        }
        context = {**context, **blogs_list}
        return context

class TopicListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6

    def get_queryset(self, **kwargs):
        topic_id = self.kwargs['pk']
        posts = Post.objects.filter(topic = topic_id)
        return posts

    def get_context_data(self, **kwargs):
        title = int(self.kwargs['pk'])
        blogs_list = super().get_context_data(**kwargs)
        topic = Topics.objects.all()
        context = {
            'blogs_list': blogs_list,
            'posts': blogs_list['object_list'],
            'title': title,
            'topics': topic
        }
        context = {**context, **blogs_list}
        return context

def error_404_view(request, exception):

    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')
