from rest_framework import serializers

from .models import Board, Column, Task, Membership


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description')


class ColumnSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Column
        fields = ('title', 'tasks')


class BoardSummarySerializer(serializers.ModelSerializer):
    owner = serializers.CharField()
    
    class Meta:
        model = Board
        fields = ('title', 'description', 'owner', 'is_public')
        read_only_fields = ('owner',)


class BoardDetailSerializer(serializers.ModelSerializer):
    owner = serializers.CharField()
    member = serializers.CharField()
    columns = ColumnSerializer(many=True)

    class Meta:
        model = Board
        fields = ('title', 'description', 'owner', 'is_public', 'member', 'columns')
