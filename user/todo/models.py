from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TodoModel(models.Model):
    task=models.CharField(max_length=250)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}-{}".format(self.user,self.task)
    
    class Meta:
        ordering=['-created']