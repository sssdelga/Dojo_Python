from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['name'])<5:
            errors['name']="Course name should be at least 5 characters"
        if len(post_data['desc'])<15:
            errors['desc']="Description should be at least 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    objects = CourseManager()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
