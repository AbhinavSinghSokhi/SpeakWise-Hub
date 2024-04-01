from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class paragraph(models.Model):
    para_num= models.IntegerField(unique= True)
    paragraph=models.TextField()

    def __str__(self):
        return f"Paragraph {self.para_num}"