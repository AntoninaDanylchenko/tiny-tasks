from django.urls import path

from todo.views import (TaskListView,
                        TaskCreateView,
                        TaskUpdateView,
                        TaskDeleteView,
                        TagListView,
                        TagCreateView,
                        TagUpdateView,
                        TagDeleteView)


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task-create/", TaskCreateView.as_view(), name="task-create"),
    path("task-update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task-del/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tag-create/", TagCreateView.as_view(), name="tag-create"),
    path("tag-update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tag-del/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
