from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags").order_by("done", "-created")
    paginate_by = 5

class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:tasks_list")
    template_name = "todo/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "todo/task_form.html"
    fields = "__all__"
    success_url = reverse_lazy("todo:tasks_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:tasks_list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tags_list")
    template_name = "todo/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "todo/tag_form.html"
    fields = "__all__"
    success_url = reverse_lazy("todo:tags_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tags_list")


class TaskToggleDoneView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save()
        return redirect("todo:tasks_list")
