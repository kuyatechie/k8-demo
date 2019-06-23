from django.db import models

# Create your models here.
class Attendance(models.Model):
    login = models.DateTimeField(null=False)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    gate = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ('id', )
