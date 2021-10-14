from mongoengine import Document, fields


class Person(Document):
    created = fields.DateTimeField(auto_now_add=True)
    last_modified = fields.DateTimeField(auto_now=True)
    first_name = fields.StringField(max_length=100, blank=False)
    last_name = fields.StringField(max_length=100, blank=False)
    email = fields.EmailField(blank=False)
    github = fields.StringField(max_length=100, blank=False)
    date_joined = fields.DateField()
    profile_pic = fields.StringField(max_length=100, blank=True)


class Note(Document):
    created = fields.DateTimeField(auto_now_add=True)
    last_modified = fields.DateTimeField(auto_now=True)
    content = fields.StringField()
    person = fields.ReferenceField(Person)
    facilitator = fields.ReferenceField(Person)
