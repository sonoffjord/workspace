from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, related_name='board_owner', on_delete=models.CASCADE)
    member = models.ManyToManyField(User, related_name='boards', through='Membership', blank=True, null=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f'Owner - {self.owner} :: Board Title - {self.title}'


class Column(models.Model):
    title = models.CharField(max_length=255)
    board = models.ForeignKey(Board, related_name='columns', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Board - {self.board} :: Column - {self.title}'


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    column = models.ForeignKey(Column, related_name='tasks', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.column.board} :: {self.column} :: {self.title}'


class UserRole(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    can_edit = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Membership(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_query_name='memberships')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_query_name='memberships')
    role = models.ForeignKey(UserRole, on_delete=models.PROTECT, related_query_name='memberships')
