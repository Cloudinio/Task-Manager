from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from main.models import Task


def Hello(request):
    return HttpResponse("Привет, это мое дз :)")

class TaskListView(ListView):
    model = Task
    template_name = "main/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        qs = (Task.objects
                    .select_related("category", "user")
                    .order_by(*Task._meta.ordering))
        
        #если в ручке передается status, categort_id, то фильтрация по ним
        status = self.request.GET.get("status")
        category_id = self.request.GET.get("category")
        if status:
            qs = qs.filter(status=status)
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs
    
class TaskDetailView(DetailView):
    model = Task
    template_name = "main/task_detail.html"
    context_object_name = "task"
