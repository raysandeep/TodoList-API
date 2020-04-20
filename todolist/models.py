from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
'''
{
    'id':'',
    'user':'',
    'time':'',
    'task_heading':'',
    'task_detail':'',
    'completed':false
}

'''


class TasksModel(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task_heading = models.CharField(max_length=100)
    task_detail = models.TextField()
    status = models.BooleanField(default=False)
