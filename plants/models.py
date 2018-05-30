from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Plant(models.Model):
    plant_name = models.CharField(max_length=100)
    img_src = models.ImageField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.plant_name
