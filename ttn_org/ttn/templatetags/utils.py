from django.core.serializers import serialize
from django.db.models.query import QuerySet
import simplejson
from django.template import Library

register = Library()

#register.filter('jsonify', jsonify)
