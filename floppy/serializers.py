from rest_framework import serializers
from rest_framework.request import Request
from .models import Note

class NoteSerializer(serializers.HyperlinkedModelSerializer):

    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'date_created', 'date_modified']

    def create(self, validated_data):
        user = self.context['request'].user  
        validated_data['owner_id'] = user.id
        note = super(NoteSerializer, self).create(validated_data)
        note.save()

        return note 