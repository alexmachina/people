from rest_framework_mongoengine import serializers
from core.models import Person, Note


class PersonSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Person
        fields = [
            "created",
            "last_modified",
            "first_name",
            "last_name",
            "email",
            "github",
            "date_joined",
            "profile_pic",
        ]


class NoteSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Note
        fields = ["created", "last_modified", "content", "person", "facilitator"]
