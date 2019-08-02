from django.shortcuts import render
from bab_app.models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

    