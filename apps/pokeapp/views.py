from django.shortcuts import render, redirect,HttpResponse
from . models import User, Poke
from collections import Counter
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
        userid=[]
        seenid=[]
        names={}
        users={}


        loginuser=User.objects.get(id=request.session['logged_in'])
        userrows=User.objects.all().exclude(id=request.session['logged_in'])
        rows=Poke.objects.filter(receivedpoke=request.session['logged_in'])



        for i in rows:
            userid.append(i.poked.id)

        for x in userid:
            if x not in seenid:
                seenid.append(x)
                total=Poke.objects.filter(poked=x).count()
                ns=Poke.objects.filter(poked=x)
                n=ns[0].poked.name
                b="{} poked you {} times!".format(n,total)
                names[x]=b

        for y in userrows:
            print "*"*50
            a=y.name
            b=y.alias
            c=y.email
            d=y.receivedpoke.all().count()
            e="{}{}{}{}".format(a,b,c,d)
            users[y]=e
        context = {
                "loginuser":loginuser,
                "users":users,
                "names":names,
        }
        return render(request, 'pokeapp/login.html',context)
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
