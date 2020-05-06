from django.db import models

class Main_menu(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    url = models.URLField()


class Category(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    url = models.URLField()
    parent_category = models.ForeignKey(Main_menu, on_delete=models.CASCADE)