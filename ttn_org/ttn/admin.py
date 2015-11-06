from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils import safestring

from .models import Gateway, Community, Post, Media, Resource, TTNUser,\
                    Company, Feed, InitiatorSubmission, KeyValue
from . import actions

admin.site.register(Media)
admin.site.register(Resource)
admin.site.register(Company)
admin.site.register(Feed)
admin.site.register(KeyValue)


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
                       'meetup_url', 'twitter_handle',
                       'image_url', 'image_thumb_url']
        }),
        ('Assets', {
            'fields': ['leaders', 'members', 'gateways', 'companies'],
            'classes': ['collapse']
        })
    ]
    filter_horizontal = ('leaders', 'members', 'gateways', 'companies')
    inlines = [PostInline, MediaInline, ResourceInline]
    list_display = ('slug', 'title', 'published', 'created')
    search_fields = ('title', 'slug', 'description')
    list_filter = ('created', 'published')


@admin.register(Gateway)
class GatewayAdmin(admin.ModelAdmin):
    list_display = ('title', 'kickstarter', 'status', 'created')
    search_fields = ('title', 'email')
    list_filter = ('created', 'kickstarter')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', 'created', 'updated')
    search_fields = ('title', 'description')


@admin.register(InitiatorSubmission)
class InitiatorSubmissionAdmin(admin.ModelAdmin):
    #def button(self):
    #    return safestring.mark_safe('<input type="...">')
    #button.short_description = 'Action'
    #button.allow_tags = True

    actions = (actions.create_community,)
    list_display = ('name', 'email', 'area', 'internal_comments', 'created',
                    'community')

