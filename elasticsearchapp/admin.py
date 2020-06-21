from django.contrib import admin

# Register your models here.
from elasticsearchapp.models import  BlogPost

admin.site.register(BlogPost)

