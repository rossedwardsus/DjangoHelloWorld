from django.db import models

# Create your models here.

#class Contract(models.Model):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)


class Question(models.Model):
    question_id = models.CharField(max_length=30)
    #user_id = models.CharField(max_length=30)
    #question_category = models.CharField(max_length=30)
    #question_title = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    datetime = models.CharField(max_length=30)
    