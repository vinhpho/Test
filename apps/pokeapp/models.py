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
        user = users[0]
        if len(users) == 0:
            messages.error(request, "The user does not exist")
            is_valid = False
            return is_valid
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
        new_poke = Poke(
            poked=User.objects.get(id=request.session['logged_in']),
            receivedpoke=User.objects.get(id=request.POST['userid'])
        )
        new_poke.save()

        # users=User.objects.all().exclude(id=request.session['logged_in'])
        #
        # rows=Poke.objects.filter(receivedpoke=request.POST['userid'])
        # row=rows[0]
        # total=rows.all().count()
        #
        # new_history = History(
        #     name = row.receivedpoke.name,
        #     alias = row.receivedpoke.alias,
        #     email = row.receivedpoke.email,
        #     time = total
        # )
        # new_history.save()
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

class Poke(models.Model):
    poked = models.ForeignKey(User, related_name = 'poked',null=True)
    receivedpoke = models.ForeignKey(User, related_name = 'receivedpoke',null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class History(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    time = models.IntegerField(default=0)
