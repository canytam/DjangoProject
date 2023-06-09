from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Author, Comment, Post

class AuthorInline(admin.StackedInline):
    model = Author
    can_delete = False
    
class UserAdmin(BaseUserAdmin):
    inlines = (AuthorInline,)
    
# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Comment)
admin.site.register(Post)
