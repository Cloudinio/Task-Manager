from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from main.models import Task, Category
from django.utils.dateparse import parse_date
from main.forms import TaskForm, RegisterForm
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

def Hello(request):
    return render(request, "main/hello.html")

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "main/task_list.html"
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        qs = (Task.objects
                    .select_related("category", "user")
                    .order_by(*Task._meta.ordering))
        
        status = self.request.GET.get("status")
        category_id = self.request.GET.get("category")
        deadline_from = self.request.GET.get("deadline_from")
        deadline_to = self.request.GET.get("deadline_to")
        query = self.request.GET.get("query")

        if query:
            qs = qs.filter(Q(title__icontains=query))
        if status:
            qs = qs.filter(status=status)
        if category_id:
            qs = qs.filter(category_id=category_id)
        if deadline_from:
            date_from = parse_date(deadline_from)
            if date_from:
                qs = qs.filter(deadline__date__gte=date_from)
        if deadline_to:
            date_to = parse_date(deadline_to)
            if date_to:
                qs = qs.filter(deadline__date_lte=date_to)

        return qs
    
    # переопределяем контекст
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # все категории для выпадающего списка
        context["categories"] = Category.objects.all()
        # варианты статусов (берём из choices enum’а)
        context["statuses"] = Task.Status.choices

        # чтобы форма помнила текущие фильтры
        context["current_status"] = self.request.GET.get("status", "")
        context["current_category"] = self.request.GET.get("category", "")
        context["current_deadline_from"] = self.request.GET.get("deadline_from", "")
        context["current_deadline_to"] = self.request.GET.get("deadline_to", "")
        context["query"] = self.request.GET.get("query", "")

        return context
    
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "main/task_detail.html"
    context_object_name = "task"

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("task-list") 

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'main/task_update.html'
    context_object_name = "task"
    
    def get_success_url(self):
        return reverse_lazy("task-detail", kwargs={"pk": self.object.pk})
    
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "main/task_create.html"
    
    def get_success_url(self):
        return reverse_lazy("task-list")
    
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect("task-list")
    else:
        form = RegisterForm()

    return render(request, "main/register.html", {"form": form})