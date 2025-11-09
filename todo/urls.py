from django.urls import path

from todo.views import TaskListView, TaskCreateView, TagListView, TagCreateView


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task-create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tag-create/", TagCreateView.as_view(), name="tag-create"),
]

app_name = "todo"
