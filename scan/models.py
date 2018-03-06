from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class tasksdata(models.Model):
    taskname = models.CharField(max_length=500, verbose_name='任务名称')
    taskdata = models.CharField(max_length=500, verbose_name='主域名')
