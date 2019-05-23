from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


# posts = [
#     {
#         'author': 'mansoor',
#         'title': 'nothing',
#         'content': 'first post',
#         'date_posted': '2018'
#     },
#     {
#         'author': 'sara',
#         'title': 'heelo',
#         'content': 'second post',
#         'date_posted': '2019'
#     },
# ]


def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html',context)


def about(request):
    context={
        'title':'about'
    }
    return render(request, 'blog/about.html', context)
