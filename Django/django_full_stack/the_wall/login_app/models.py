from django.db import models
import re

class UserManager(models.Manager):
    def reg_validate(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email']='Invalid email entered'
        if len(post_data['first_name'])<2:
            errors['first_name']='First name must be at least two characters'
        if len(post_data['last_name'])<2:
            errors['last_name']='Last name must be at least two characters'
        if len(post_data['password'])<8:
            errors['password']='Password must be at least eight characters'
        if post_data['password']!=post_data['password_confirm']:
            errors['password']='Passwords did not match'
        return errors
    def login_validate(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email']='Invalid email entered'
        if len(post_data['password'])<8:
            errors['password']='Invalid password entered'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
