from django.db import models

class Category(models.Model):
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.description

class Serie(models.Model):
    name = models.CharField(max_length=100)
    realese_date = models.DateField()
    rating = models.IntegerField(default=0)
    cotegory = models.ForeignKey(Category, on_delete=models.CASCADE)
    