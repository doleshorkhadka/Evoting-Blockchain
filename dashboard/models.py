from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    slogan = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" + self.email

    