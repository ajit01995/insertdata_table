from django.db import models

# Create your models here.

class Topic(models.Model):
    Topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self) -> str:
        return self.Topic_name
    
class Webpage(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    def __str__(self) -> str:
        return self.name

