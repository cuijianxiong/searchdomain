from django.shortcuts import render
from django.http import HttpResponseRedirect
from random import Random

def random_str(randomlength=29):   #random cookie
    cook = ''
    chars = '_AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        cook+=chars[random.randint(0, length)]
    return cook

# Create your views here.
def index(request):
    return render(request, 'index.html', locals())

def domain(request):
    return render(request, 'domain.html', locals())

def notfound(request):
    return render(request, '404.html', locals())

def login(request):
    #cookie = request.COOKIES.get('islogin')
    #username = request.COOKIES.get('username')
    #islogin = User.objects.filter(username__exact=username, cookie__exact=cookie)
    #return HttpResponseRedirect('/login.html')
    return render(request, 'login.html', locals())