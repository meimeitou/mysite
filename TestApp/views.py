from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404 , render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views import generic
# Create your views here.
#from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import UploadFileForm

def files(request):
	if request.method=='POST':
		myfile=request.FILES.get('myfile',None)
		name=request.POST['name']
		#if not myfile:
		if myfile:
			handle_uploaded_file(myfile)
		import os
		path=os.path.abspath('.')
		
		return render(request,'TestApp/files.html',{'message':request.COOKIES,'name':myfile.name if myfile else 'no file'})
		#else :
		#	return HttpResponseRedirect('TestApp/uploadths/')
		#return render_to_response('TestApp/files.html')
    
	return render(request,'TestApp/files.html',{})

def  ths(request):
	return render_to_response('TestApp/success.html')
	#instance=RequestContext(request)
	
	#return render_to_response('TestApp/success.html',{'message':'updone!'})
def search_form_post(request):
    car_list = None

    if 'q' in request.POST:
        message = '你搜索的是: %r' % request.POST['q']
        if 'chk_contains' in request.POST:
            car_list = Car.objects.filter(brand__contains=request.POST['q'])
        else:
            car_list = Car.objects.filter(brand=request.POST['q'])
    else:
        message = '请输入要搜索的内容并点击搜索'

    return render(request, "search_form_post.html", {'message': message, 'car_list': car_list})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('static/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)