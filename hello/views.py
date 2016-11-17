from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime
from . import forms

def hello_forms(request):
    form = forms.HelloForm(request.GET or None)
    if form.is_valid():
        message = 'データ検証に成功しました'
    else:
        message = 'データ検証に失敗しました'
    d = {
        'form': form,
        'message': message,
    }
    return render(request, 'forms.html', d)

def hello_forms2(request):
    d = {
        'form': forms.SampleForm(),
    }
    return render(request, 'form_sample.html', d)

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

def hello_for(request):
    d = {
      'objects': range(10),
    }
    return render(request, 'for.html', d)

def hello_get_query(request):
    d = {
        'your_name': request.GET.get('your_name')
    }
    return render(request, 'get_query.html', d)
