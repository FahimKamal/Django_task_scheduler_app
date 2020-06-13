from django.db import models


# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FamilyRole(models.Model):
    role = models.CharField(max_length=30)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.role


class Person(models.Model):
    Name = models.CharField(max_length=50)
    age = models.IntegerField()
    family = models.ForeignKey(FamilyRole, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.Name

