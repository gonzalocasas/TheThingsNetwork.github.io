from django.utils import text as utils_text
from django.contrib.auth.models import User
from .models import Gateway, Community, Post, Media, Resource


def send_email(todo):
    pass

def create_user(email, username=None, send_activation_email=False, **kwargs):
    existing = User.objects.filter(email=email)
    if existing:
        return existing[0]
    # Try superhard to get him/her a nice username
    if not username:
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        try_names = [first_name, "{} {}".format(first_name, last_name),
                     last_name, email.split('@')[0]]
        try_names += ["{}{}".format(first_name, c) for c in range(100)]
        for uname in try_names:
            uname = utils_text.slugify(uname)
            if not len(User.objects.filter(username=uname)):
                username = uname
                break
        
    user = User(username=username, email=email, **kwargs)
    user.save()
    #user = User.objects.filter(email=email)
    print("CREATED USER", user, 'WITH', email, username, kwargs)
    if send_activation_email:
        send_email("TODO")
    return user
