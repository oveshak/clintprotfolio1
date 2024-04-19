from django.contrib import admin

from post.models import About,Blog ,Hero
# Register your models here.
admin.site.register(Hero)
admin.site.register(About)
admin.site.register(Blog)
