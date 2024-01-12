from django.db import models

class TODO(models.Model):
    task_name = models.CharField(max_length=50,null= True)
    task_date = models.DateField(null = True)
    task_detail = models.CharField(max_length = 100, null=True)
    status = models.BooleanField(default ="True")
    def __str__(self):
        return self.task_name

