from django.contrib import admin

from post.models import About,Blog ,Hero,ExperienceandEducation,ExperienceandEducationResume,Skill,SkillResume
# Register your models here.
admin.site.register(Hero)
admin.site.register(About)
admin.site.register(Blog)
admin.site.register(ExperienceandEducation)
admin.site.register(ExperienceandEducationResume)
admin.site.register(Skill)
admin.site.register(SkillResume)