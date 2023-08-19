from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Prefetch
from django.contrib.auth.models import User
from django.db.models import OuterRef, Subquery

from .models import Board, Column, Task, Membership
from .serializers import BoardSummarySerializer, BoardDetailSerializer, ColumnSerializer, TaskSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()

    def get_queryset(self):
        if self.action == 'list':
            return Board.objects.select_related(
                'owner'
            ).only(
                'id',
                'title',
                'description',
                'is_public',
                'owner__username',
                'owner__id',
            )
        
        if self.action == 'retrieve':
            return Board.objects.all().select_related(
                'owner'
            ).prefetch_related(
                Prefetch('member', queryset=User.objects.all().only('username', 'id')),
                'columns',
                'columns__tasks',
            ).only(
                'id',
                'title',
                'description',
                'is_public',
                'owner__username',
                'owner__id',
                'member__username'
            )

        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'create':
            return BoardSummarySerializer
        return BoardDetailSerializer

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()
