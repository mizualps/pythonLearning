from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime

# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World!')

'''
def hello_template(request):
    return render(request, 'index.html')
'''

def hello_template(request):
    d = {
      'hour': datetime.now().hour,
      'message': 'sample messsage',
    }
    return render(request, 'index.html', d);

def hello_if(request):
    d = {
      'is_visible': False,
      'empty_str': '',
    }
    return render(request, 'if.html', d)
