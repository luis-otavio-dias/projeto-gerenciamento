from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Navigators(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Students(models.Model):
    stage_choices = (
        ("E1", "10-100k"),
        ("E2", "100-1kk"),
        ("E3", "1-10kk"),
    )
    name = models.CharField(max_length=50)
    picture = models.ImageField(
        upload_to="pictures",
        null=True,
        blank=True,
    )
    stage = models.CharField(
        max_length=2,
        choices=stage_choices,
    )
    navigator = models.ForeignKey(
        Navigators,
        null=True,
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_in = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
