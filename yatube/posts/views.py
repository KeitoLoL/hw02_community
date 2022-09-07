from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):

    posts = Post.objects.all()[:settings.DISPLAYS_NUMBER]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):

    template = 'posts/group_list.html'
    group = get_object_or_404(Group.objects.all().prefetch_related('groups'), slug=slug)
    posts = group.groups.all()
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
