from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
# Create your views here.
import datetime


def hello(request):
    now = datetime.datetime.now()
    test_str="show"
    return render_to_response('hellow.html', {'current_date': now,'test_str': test_str})


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def current_time(request):
    now = datetime.datetime.now()
    t = get_template('hellow.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def curtent_time2(request):
    now = datetime.datetime.now()
    return render_to_response('hellow.html', {'current_date': now})
