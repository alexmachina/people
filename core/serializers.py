from rest_framework import serializers
from core.models import Person, Note


class PersonSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    facilitator_notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

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
            "notes",
            "facilitator_notes",
        ]


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["created", "last_modified", "content", "person", "facilitator"]
