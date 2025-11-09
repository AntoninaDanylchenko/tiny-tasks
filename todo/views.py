from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from todo.models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)