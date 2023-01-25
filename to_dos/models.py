from django.db import models

class Todo(models.Model):
    task= models.CharField(max_length=100)
    datetime= models.DateTimeField()
    description= models.CharField(max_length=200)
    
    #rename the instance of a model with thier title name
    def __str__(self):
        return self.task
    def __str__(self):
        return self.description

     