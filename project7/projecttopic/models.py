from django.db import models

class Project(models.Model):

    languages = (

        ('C++', 'C++'),

        ('Java', 'Java'),

        ('Python', 'Python'),

        ('Typescript', 'Typescript'),

        )
    topic = models.CharField(max_length=30)
    language = models.CharField(max_length=20, choices=languages)
    duration= models.CharField(max_length=10, help_text='Duration in Weeks')