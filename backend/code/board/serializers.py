from rest_framework import serializers

from .models import Board, Column, Task, Membership


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description')


class ColumnSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer()

    class Meta:
        model = Column
        fields = ('title', 'tasks')


class BoardSummarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Board
        fields = ('title', 'description', 'owner',)
        read_only_fields = ('owner',)


class BoardDetailSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer()

    class Meta:
        model = Board
        fields = ('title', 'description', 'owner', 'member', 'columns')
