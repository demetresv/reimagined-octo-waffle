from django.db import models


class Task(models.Model):
    STATUSES = {
        'draft': 'Draft',
        'in progress': 'In Progress',
        'completed': 'Completed'
    }

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUSES)
    description = models.TextField()

    def __str__(self):
        return self.name

