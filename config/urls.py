from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.Hello, name="hello"),
    path('admin/', admin.site.urls),
    path('tasks/', views.TaskListView.as_view(), name = "task-list"),
    path('tasks/<int:pk>', views.TaskDetailView.as_view(), name = "task-detail")
]
