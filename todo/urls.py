from django.urls import path

from todo.views import (TaskListView, TagListView, TaskCreateView,
                        TaskUpdateView, TagCreateView, TagUpdateView,
                        TaskDeleteView, TagDeleteView, TaskToggleDoneView,)

urlpatterns = [
        path("", TaskListView.as_view(), name="tasks_list"),
        path("create/", TaskCreateView.as_view(), name="task_create"),
        path("update/<int:pk>", TaskUpdateView.as_view(), name="task_update"),
        path("tags/", TagListView.as_view(), name="tags_list"),
        path("tags/create/", TagCreateView.as_view(), name="tag_create"),
        path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag_update"),
        path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
        path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
        path("<int:pk>/toggle/", TaskToggleDoneView.as_view(), name="task_toggle_done"),

]

app_name = "todo"
