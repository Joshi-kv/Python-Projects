from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=100)
    discription=models.TextField()
    year=models.IntegerField()
    image=models.ImageField(upload_to='Images')
    def __str__(self):
        return self.name