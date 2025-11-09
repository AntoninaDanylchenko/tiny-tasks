from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


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


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    success_url = reverse_lazy("todo:index")
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    context_object_name = 'tags'


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    form_class = TagForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
