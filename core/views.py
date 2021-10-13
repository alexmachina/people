from rest_framework import viewsets

from core.models import Person, Note
from core.serializers import PersonSerializer
from core.serializers import NoteSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
