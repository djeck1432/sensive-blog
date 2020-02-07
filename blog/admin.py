from django.contrib import admin
from .models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['author']


admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)