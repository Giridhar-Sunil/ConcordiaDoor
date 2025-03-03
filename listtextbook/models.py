from django.db import models

class Textbook(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('old', 'Old'),
    ]

    title = models.CharField(max_length= 300)
    year = models.IntegerField()
    edition = models.CharField(max_length=50, null=True, blank=True)
    author = models.CharField(max_length=100)
    course_code = models.CharField(max_length=9)
    availability = models.BooleanField(default=True)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='new')

    def __str__(self):
        return f'{self.title} {self.edition} by {self.author} published in {self.year} - {self.condition}'

