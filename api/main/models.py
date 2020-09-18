from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Make (models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Car (models.Model):

    make = models.ForeignKey(Make, related_name="cars", on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    owners = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.make}: {self.model}"

class Issue (models.Model):

    RECALL = "RC"
    ISSUE = "IS"
    ISSUE_TYPE_CHOICES = [
        (RECALL, "recall"),
        (ISSUE, "issue")
    ]

    car = models.ForeignKey(Car, related_name="reports", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(default="No description given")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(
        max_length=2,
        choices=ISSUE_TYPE_CHOICES,
        default=ISSUE
        )
    
    def __str__(self):
        return self.title