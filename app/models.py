from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=233)
    email = models.EmailField()
    subject = models.CharField(max_length=233)
    message = models.TextField()
    # cv = models.FileField(blank=True,null=True)


    def __str__(self) -> str:
        return self.name