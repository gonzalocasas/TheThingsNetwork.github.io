from django.contrib import admin
from .models import Gateway, Community, Post, Media, Resource

admin.site.register(Gateway)
admin.site.register(Post)
admin.site.register(Media)
admin.site.register(Resource)


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
            'fields': ['slug', 'title', 'description',
                       'lat', 'lon', 'scale',
                       'image_url', 'image_thumb_url']
        }),
        ('Assets', {
            'fields': ['leaders', 'members', 'gateways'],
            'classes': ['collapse']
        })
    ]
    inlines = [PostInline, MediaInline, ResourceInline]
    list_display = ('slug', 'title', 'created')
    search_fields = ('title', 'slug', 'description')
    list_filter = ('created',)

