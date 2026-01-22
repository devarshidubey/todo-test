from rest_framework import serializers
from todos.models.todo import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            'title',
            'description',
            'completed',
            'created_at',
            'metadata'
        ]
        read_only_fields = ['id', 'created_at', 'metadata']
        