from django.db import models

class User (models.Model):

    email = models.EmailField()
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Car (models.Model):

    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.make}: {self.model}"

class Issue (models.Model):

    RECALL = "RC"
    ISSUE = "IC"
    ISSUE_TYPE_CHOICES = [
        (RECALL, "recall"),
        (ISSUE, "issue")
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    type = models.CharField(
        max_length=2,
        choices=ISSUE_TYPE_CHOICES,
        default=ISSUE
        )
    
    def __str__(self):
        return self.title