from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from django.urls import reverse_lazy
from main import views

urlpatterns = [
    path('', views.Hello, name="hello"),
    path('admin/', admin.site.urls),
    path('tasks/', views.TaskListView.as_view(), name = "task-list"),
    path('tasks/<int:pk>', views.TaskDetailView.as_view(), name = "task-detail"),
    path('tasks/<int:pk>/delete', views.TaskDeleteView.as_view(), name = "task-delete"),
    path('tasks/<int:pk>/update', views.TaskUpdateView.as_view(), name = "task-update"),
    path('tasks/create', views.TaskCreateView.as_view(), name = "task-create"),
    path('login/', auth_views.LoginView.as_view(template_name = 'main/login.html'), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(next_page = reverse_lazy("hello")), name = "logout"),
    path("register/", views.register, name="register")
]
