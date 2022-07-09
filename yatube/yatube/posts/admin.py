from django.contrib import admin
# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)

admin.site.register(Post, PostAdmin)
