from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    class Status(models.TextChoices):
        IN_PROGRESS = "in_progress", "в работе"
        DONE = "done", "выполнено"
        TO_DO = "to_do", "к выполнению"
    
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    deadline = models.DateTimeField(null=True, blank=True, verbose_name="Дедлайн")
    status = models.CharField(max_length=20, default=Status.TO_DO, choices=Status.choices, verbose_name="Статус")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="tasks", verbose_name="Категория")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks", verbose_name="Исполнитель")
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ["-created_at"]
        
    def __str__(self) -> str:
        return self.title
