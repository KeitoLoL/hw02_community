from django.shortcuts import get_object_or_404, render

import yatube.settings as sett

from .models import Group, Post


def index(request):

    posts = Post.objects.all()[:sett.displays_number]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):

    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).all()[:sett.displays_number]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
