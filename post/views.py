from django.shortcuts import render

from post.models import About, Hero,Blog,ExperienceandEducationResume

# Create your views here.
def index(request):
    hero=Hero.objects.all()[0]
    about=About.objects.all()[0]
    blog=Blog.objects.all()
    experience=ExperienceandEducationResume.objects.filter(type="EXPRTIENCE")[0]
    education=ExperienceandEducationResume.objects.filter(type="EDUCATION")[0]
    context={
        "hero":hero,
        "about":about,
        "blog":blog,
        "experiences":experience,
        "educations":education,
    }
    return render(request,'post/index.html',context)