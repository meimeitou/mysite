__author__ = 'yinqiwei'

from django import template


register=template.Library()

@register.filter(name='cut')
def  cut(value,arg):
	return value.replace(arg,'')
@register.filter()
def lower(value):
	return value.lower()

'''
等价
自定义过滤器 首先定义函数 然后用library实例注册过滤器

def cut(value,arg)
    return value.replace(arg,'')
register.filter('cut',cut)
'''