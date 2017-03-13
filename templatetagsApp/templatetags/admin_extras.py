__author__ = 'yinqiwei'
from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '_')


def mylower(value):
    return value.lower()

#register.filter('cut', cut)
register.filter('mylower', mylower)