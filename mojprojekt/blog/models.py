from django.db import models
from django.contrib import admin

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    czas = models.DateTimeField()    

    class Meta:
        ordering = ('-czas', )
        
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','czas')

admin.site.register(BlogPost, BlogPostAdmin)