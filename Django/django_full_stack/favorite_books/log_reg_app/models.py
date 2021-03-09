from django.db import models
import re

class UserManager(models.Manager):
    def reg_validate(self, post_data):
        errors = {}
        if len(post_data['first_name'])<2:
            errors['first_name']="First name must be at least 2 characters"
        if len(post_data['last_name'])<2:
            errors['last_name']="Last name must be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email']="Invalid email address entered"
        if len(post_data['password'])<8:
            errors['password']="Password must be at least 8 characters"
        if post_data['password']!=post_data['password_confirm']:
            errors['password']="Passwords did not match"
        return errors
    def login_validate(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email']="Invalid email address entered"
        if len(post_data['password'])<8:
            errors['password']="Invalid password entered"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

#################################################################################
#################################################################################

class BookManager(models.Manager):
    def book_validate(self, post_data):
        errors = {}
        if len(post_data['title'])<1:
            errors['title']="A title must be provided"
        if len(post_data['desc'])<5:
            errors['desc']="Description must be at least 5 characters"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User, related_name='added_books', on_delete=models.CASCADE)
    favorites = models.ManyToManyField(User, related_name='fav_books')
    objects = BookManager()