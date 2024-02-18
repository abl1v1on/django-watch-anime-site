from django import template

from ..models import Comments
from ..utils import get_all_comments

register = template.Library()

@register.simple_tag()
def tag_new_comments():
    return get_all_comments().order_by('-id')[:6]
