from django.contrib import admin

from .models import Snippet

from .models import Article
# Register your models here.

admin.site.register(Snippet)
admin.site.register(Article)


