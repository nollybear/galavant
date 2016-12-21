from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from bcrypt import hashpw
from itertools import count


class UserManager(models.Manager):
    def register(self, first_name, last_name, email, password, confirm):
        errors = []
        EMAIL_REGEX = (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(first_name) <= 2:
            errors.append("A first name with at least two character is required")
        if len(last_name) <= 2:
            errors.append("A last name with at least two character is required")
        if len(password) == 0:
            errors.append("Password is required")
        elif password != confirm:
            errors.append("Password and confrimation must match")
        if len(email) == 0:
            errors.append("Email is required")
        elif not re.match(EMAIL_REGEX, email):
            errors.append("Valid email is required")
        if len(errors) is not 0:
            return (False, errors)
        else:
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            Users = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = hashed)
            return True

    def login(self, email, password):
            errors = []
            print "this is the login function in the class", email
            print "this is the login function in the class", password
            if User.objects.filter(email=email):
                user = User.objects.filter(email=email)[0]
                print "PRINT USER IN LOGIN METHOD", user
                hashed = user.password
                if bcrypt.hashpw(password.encode(), hashed.encode()) == hashed:
                    loggedin = "Successfully created new user"
                    return True
                else:
                    errors.append("Invalid password for this email")
                    return (False, errors)
            else:
                errors.append("Invalid login credentials")
                return (False, errors)

class User(models.Model):
    first_name = models.CharField(max_length=45, default='null')
    last_name = models.CharField(max_length=45, default='null')
    email = models.CharField(max_length=45, default='null')
    password = models.CharField(max_length=255, default='null')
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()


# class TrailManager(models.Manager):
#     def addtrail (self, lat, long, ):
#         response = unirest.get("https://trailapi-trailapi.p.mashape.com/?lat=34.1&limit=25&lon=-105.2&q[activities_activity_name_cont]=Yellow+River+Trail&q[activities_activity_type_name_eq]=hiking&q[city_cont]=Denver&q[country_cont]=Australia&q[state_cont]=California&radius=25",
#   headers={
#     "X-Mashape-Key": "1u15iOxcOamshAqge8yv6lHqQptQp1QMZh1jsn5z4nFcYcRRzd",
#     "Accept": "text/plain"
#   }
# )
#
# --get --include 'https://trailapi-trailapi.p.mashape.com/' \
#   -H 'X-Mashape-Key: 1u15iOxcOamshAqge8yv6lHqQptQp1QMZh1jsn5z4nFcYcRRzd' \
#   -H 'Accept: text/plain'
#
# class Trail(models.Model):
#     name = models.CharField(max_length=45, default='null')
#     city = models.CharField(max_length=45, default='null')
#     lat = models.IntegerField(default='null')
#     lon = models.IntegerField(default='null')
#     activity = models.CharField(max_length=45, default='null')
#     country = models.CharField(max_length=45, default='null')
#     state = models.CharField(max_length=45, default='null')
#     objects = TrailManager()
