from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from todo.models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        return (super().get_queryset()
                .filter(user=self.request.user)
                .select_related('user')
                .prefetch_related('tags')
                .order_by('is_completed', 'deadline', '-created_at'))