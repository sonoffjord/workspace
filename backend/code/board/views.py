from rest_framework import viewsets

from .models import Board, Column, Task, Membership
from .serializers import BoardSummarySerializer, BoardDetailSerializer, ColumnSerializer, TaskSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return BoardSummarySerializer
        return BoardDetailSerializer

