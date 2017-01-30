from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import bcrypt
# Create your models here.
class UserManager(models.Manager):
    def createuser(self,request):
        is_valid = True
        if len(request.POST['name']) == 0:
            is_valid = False
            messages.error(request,'First Name is required.')
        if len(request.POST['alias'])== 0:
            is_valid = False
            messages.error(request,'Alias is required.')
        if len(request.POST['bday'])== 0:
            is_valid = False
            messages.error(request,'Birthday is required.')
        if len(request.POST['email']) == 0:
            is_valid = False
            messages.error(request,'Email is required.')
        email_check = User.objects.filter(email=request.POST['email'])
        if len(email_check) > 0:
            is_valid= False
            messages.error(request, 'Email is already exist')
        if len(request.POST['password'])< 8:
            is_valid = False
            messages.error(request, 'Password requires at least 8 characters')
        if request.POST['password'] != request.POST['confirm_password']:
            messages.error(request, 'Password and confirm password do not match')
            is_valid = False
        if not is_valid:
            return is_valid
        hashed = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
        new_user = User(
            name=request.POST['name'],
            alias = request.POST['alias'],
            bday = request.POST['bday'],
            email=request.POST['email'],
            password=hashed,
        )
        new_user.save()
        request.session['logged_in'] = new_user.id;
        is_valid = True
        return is_valid

    def login(self,request):
        is_valid = True
        users= User.objects.filter(email=request.POST['email'])
        if len(users) == 0:
            messages.error(request, "The user does not exist")
            is_valid = False
            return is_valid
        user = users[0]
        dbpw=bcrypt.hashpw(request.POST['password'].encode('utf-8'), user.password.encode('utf-8'))
        if dbpw != user.password:
            messages.error(request, "Either email or password is incorrect")
            is_valid = False
            return is_valid
        #when password is correct
        request.session['logged_in'] = user.id
        return is_valid

    def logout(self,request):
        is_valid=True
        del request.session['logged_in']
        return True

    def createpokes(self,request):
        print"*"*50
        print request.POST['userid']
        lusers=User.objects.filter(id=request.session['logged_in'])
        beingpokes=User.objects.filter(id=request.POST['userid'])
        beingpoke=beingpokes[0]
        luser=lusers[0]

        request.session['pokeid'] = request.POST['userid']

        print beingpoke.id
        print beingpoke.name
        # if 'pokeid' not in request.session:
        #     if 'count' not in request.session:
        #         request.session['count]' = 0
        #     else:
        #         request.session['count]' = request.session['count]' + 1
        # print count
        print"*"*50
        new_poke = poke(
            name = beingpoke.name
            # pokecount = count
        )
        new_poke.save()
        loggeduser.pokes.add(new_poke)

        new_history = History(
            name = luser.name,
            alias = luser.alias,
            email = luser.email,
            poke = beingpoke.name
        )
        new_history.save()
        return True

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    bday = models.DateField(auto_now=False, auto_now_add=False)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class poke(models.Model):
    name = models.CharField(max_length=255)
    pokes = models.ManyToManyField(User)

class History(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pokes = models.CharField(max_length=255)
