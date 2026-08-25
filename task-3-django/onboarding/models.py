from django.db import models


class StudentOnboarding(models.Model):
    REGION_CHOICES = [
        ("IN-WEST", "India West"),
        ("IN-EAST", "India East"),
        ("IN-NORTH", "India North"),
        ("IN-SOUTH", "India South"),
    ]

    student_id = models.CharField(max_length=20, unique=True)
    student_name = models.CharField(max_length=100)
    region = models.CharField(max_length=10, choices=REGION_CHOICES)
    requires_support = models.BooleanField()

    def __str__(self):
        return f"{self.student_id} - {self.student_name}"