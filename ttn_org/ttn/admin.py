from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Gateway, Community, Post, Media, Resource, TTNUser,\
                    Company, InitiatorSubmission

admin.site.register(Gateway)
admin.site.register(Post)
admin.site.register(Media)
admin.site.register(Resource)
admin.site.register(Company)


# Users
class TTNUserInline(admin.StackedInline):
    model = TTNUser
    can_delete = False
    verbose_name_plural = "TTNUser"


class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'is_staff', 'date_joined', 'last_login')
    inlines = (TTNUserInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# Communities and assets
class PostInline(admin.TabularInline):
    model = Post
    extra = 0


class MediaInline(admin.TabularInline):
    model = Media
    extra = 0


class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 0


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['published', 'slug', 'title', 'mission',
                       'description', 'contact',
                       'lat', 'lon', 'scale',
                       'image_url', 'image_thumb_url']
        }),
        ('Assets', {
            'fields': ['leaders', 'members', 'gateways', 'companies'],
            'classes': ['collapse']
        })
    ]
    filter_horizontal = ('leaders', 'members', 'gateways', 'companies')
    inlines = [PostInline, MediaInline, ResourceInline]
    list_display = ('slug', 'title', 'created')
    search_fields = ('title', 'slug', 'description')
    list_filter = ('created',)


@admin.register(InitiatorSubmission)
class InitiatorSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'area', 'created')

