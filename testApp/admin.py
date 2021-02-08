from django.contrib import admin
from testApp.models import Post,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','auther','body','publish','created','updated','status']
    list_filter=('status','auther','publish','created','updated')
    search_fields=('title','body')
    raw_id_fields=('auther',)
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display1=['name','email','pos','created','updated','active']
    list_filter=('active','created','updated')
    search_fields=('name','email','body')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
