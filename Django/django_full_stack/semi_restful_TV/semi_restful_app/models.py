from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['title'])<2:
            errors['title']="Title name should be at least 2 characters"
        if len(post_data['network'])<3:
            errors['network']="Network name should be at least 3 characters"
        if len(post_data['description'])<10:
            errors['description']="Description should be at least 10 characters"

class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    release_date=models.DateTimeField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ShowManager()