from django.db import models
#giving the names to teh columns
class Student(models.Model):
    roll = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    student_class = models.CharField(max_length=20)
    total = models.IntegerField()
    paid = models.IntegerField()
    balance = models.IntegerField()

    def __str__(self):
        return self.name