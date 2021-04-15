from django.db import models

# Create your models here.
class Admin(models.Model):
    admin_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.admin_name

class Teacher(models.Model):
    admin_name=models.ForeignKey(Admin, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    url=models.URLField(max_length=100)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date=models.DateField()

