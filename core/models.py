from django.db import models


class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    github = models.CharField(max_length=100, blank=False)
    date_joined = models.DateField()
    profile_pic = models.CharField(max_length=100, blank=True)


class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    content = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.RESTRICT, related_name="notes")
    facilitator = models.ForeignKey(
        Person, on_delete=models.RESTRICT, related_name="facilitator_notes"
    )
