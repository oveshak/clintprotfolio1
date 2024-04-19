from django.shortcuts import render

from post.models import About, Hero,Blog

# Create your views here.
def index(request):
    hero=Hero.objects.all()[0]
    about=About.objects.all()[0]
    blog=Blog.objects.all()
    context={
        "hero":hero,
        "about":about,
        "blog":blog,
    }
    return render(request,'post/index.html',context)