from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.Hello, name="hello"),
    path('admin/', admin.site.urls),
    path('tasks/', views.TaskListView.as_view(), name = "task-list"),
    path('tasks/<int:pk>', views.TaskDetailView.as_view(), name = "task-detail"),
    path('tasks/<int:pk>/delete', views.TaskDeleteView.as_view(), name = "task-delete"),
    path('tasks/<int:pk>/update', views.TaskUpdateView.as_view(), name = 'task-update'),
    path('tasks/create', views.TaskCreateView.as_view(), name = "task-create")
]
