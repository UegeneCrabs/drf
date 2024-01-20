from django.db import models

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название магазина")
    owner = models.CharField(max_length=100, verbose_name="Владелец")
    token = models.CharField(max_length=8, unique=True, verbose_name="Токен", default='')

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Task(models.Model):
    TASK_TYPES = (
        ('ToDo', 'Нужно сделать'),
        ('InProgress', 'В работе'),
        ('Done', 'Сделано'),
    )
    task_type = models.CharField('Тип', max_length=20, choices=TASK_TYPES)
    task_name = models.CharField(max_length=255, verbose_name="Название задачи")
    task_description = models.TextField(blank=True, verbose_name="Описание задачи")
    task_members = models.TextField(blank=True, verbose_name="Участники")
    days_to_complete = models.PositiveIntegerField(verbose_name="Дней для выполнения")
    date_creation = models.DateTimeField(auto_now_add=False, verbose_name="Дата создания")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name="Магазин")

    def str(self):
        return self.task_name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def delete_task(self):
        self.delete()

