from ..models import Category, Tag, Friend
from django import template
from datetime import datetime

register = template.Library()

# @register.simple_tag
# def get_updated_blogs(num=5):
#     return Blog.objects.filter(status='completed').order_by('-updatetime')[:num]

# @register.simple_tag
# def archives():
#     return Blog.objects.dates('timestamp', 'month', order='DESC')

@register.simple_tag
def categories():
    return Category.objects.all()

@register.simple_tag
def tags():
    return Tag.objects.all()

@register.simple_tag
def friends():
    return Friend.objects.all()

@register.simple_tag
def nowtime():
    return datetime.now()
