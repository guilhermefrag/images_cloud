from django.db import models

# Create your models here.
class Photos(models.Model):
    id = models.AutoField(primary_key=True)
    photo_name = models.CharField(max_length=200)
    photo_file = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.photo_name

        