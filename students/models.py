from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
import secrets


# Create your models here.
class Navigators(models.Model):
    class Meta:
        verbose_name = "Navigators"
        verbose_name_plural = "Navigators"

    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Students(models.Model):
    class Meta:
        verbose_name = "Students"
        verbose_name_plural = "Students"

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
    token = models.CharField(max_length=16, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_unique_token()
        super().save(*args, **kwargs)

    def generate_unique_token(self):
        while True:
            token = secrets.token_urlsafe(8)
            if not Students.objects.filter(token=token).exists():
                return token

    def __str__(self):
        return self.name


class ScheduleAvailability(models.Model):
    class Meta:
        verbose_name = "ScheduleAvailability"
        verbose_name_plural = "ScheduleAvailabilities"

    initial_date = models.DateTimeField(null=True, blank=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    scheduled = models.BooleanField(default=False)

    def final_date(self):
        return self.initial_date + timedelta(minutes=50)


class Meeting(models.Model):
    tag_choices = (
        ("G", "Gestão"),
        ("M", "Marketing"),
        ("RH", "Gestão de pessoas"),
        ("I", "Impostos"),
    )

    date = models.ForeignKey(ScheduleAvailability, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    tag = models.CharField(max_length=2, choices=tag_choices)
    description = models.TextField()


class Task(models.Model):
    student = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    task = models.CharField(max_length=255)
    executed = models.BooleanField(default=False)


class Upload(models.Model):
    student = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    video = models.FileField(upload_to="videos")
