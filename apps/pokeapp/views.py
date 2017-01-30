from django.shortcuts import render, redirect,HttpResponse
from . models import User
# Create your views here.
def index(request):
    return render(request, 'pokeapp/index.html')
def createuser(request):
    did_create = User.objects.createuser(request)
    if did_create:
        return redirect('/main')
    else:
        return redirect('/main')
def login(request):
    did_login = User.objects.login(request)
    if did_login:
        return redirect('/main/success')
    else:
        return redirect('/main')
def success(request):
    if 'logged_in'in request.session:
        loginuser=User.objects.get(id=request.session['logged_in'])
        users=User.objects.all().exclude(id=request.session['logged_in'])
        context = {
            "loginuser":loginuser,
            "users":users,
        }
        return render(request, 'pokeapp/pokes.html',context)
    else:
        return HttpResponse("Please check username and password")
        return redirect('/main')
def pokes(request):
    did_post = User.objects.createpokes(request)
    if did_post:
        return redirect('/main/success')
    else:
        return redirect('/main')

def logout(request):
    try:
        del request.session['logged_in']
    except KeyError:
        pass
    return HttpResponse("You're successfully logged out.")
    return redirect('/main')
