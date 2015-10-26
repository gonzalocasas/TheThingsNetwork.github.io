from django.utils import text as utils_text
from . import utils
from .models import Gateway, Community, Post, Media, Resource, TTNUser,\
                    Company, Feed, InitiatorSubmission

def create_community(modeladmin, request, queryset):
    errors = []
    messages = []
    for submission in queryset:
        if submission.community:
            errors.append("Community already created for {}!".format(submission))
        else:
            # Create leader
            names = submission.name.split()
            first_name = names[0] if len(names) else ""
            last_name = " ".join(names[1:]) if len(names) > 1 else ""
            user = utils.create_user(email=submission.email,
                first_name=first_name, last_name=last_name)
            # Create community
            com = Community()
            com.title = submission.area
            slug = utils_text.slugify(com.title)
            while Community.objects.filter(slug=slug):
                slug += "1"
            com.slug = slug
            com.published = False
            com.mission = """>>> mission of your campaign in 1 sentence:
what you want to accomplish and why. For example:
'On a mission to provide {} with a free IOT data network! <<<""".format(
                com.title)
            com.description = """>>> more information about your campaign, your team and your goals. Get people excited! <<<"""
            com.contact = """>>> tell how people can contact you, e.g. the forum, twitter, facebook, mail address, telephone number <<<"""
            com.image_thumb_url = "https://scontent-ams2-1.xx.fbcdn.net/hphotos-xpa1/v/t1.0-9/11231684_416801021852414_3569271766822687136_n.png?oh=c35b7ce24f55464e0564901b624e7372&oe=56699D38"
            com.save()
            com.leaders.add(user)
            com.members.add(user)
            # Add some initial sources
            com.media_set.create(title='The Next Web - The Things Network wants to make every city smart', url='http://thenextweb.com/insider/2015/08/19/the-things-network-wants-to-make-every-city-smart-starting-with-amsterdam/', author=user)
            com.resource_set.create(title='Forum', url='http://forum.thethingsnetwork.org/', author=user)
            # Connect to submission
            submission.community = com
            submission.save()

            messages.append('Created {} community page! slug={}'.format(
                com.title, com.slug))
    return errors, messages
create_community.short_description = "Create community landing page"

