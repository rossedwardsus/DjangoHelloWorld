from datetime import datetime
import uuid
from django.db import models

# Create your models here.

#class Contract(models.Model):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)


class Question(models.Model):
    question_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    #user_id = models.CharField(max_length=30)
    #question_category = models.CharField(max_length=30)
    #question_title = models.CharField(max_length=30)
    question_title = models.CharField(max_length=30)
    question_text = models.TextField(max_length=30)
    question_added_datetime = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = "questions"
        ordering=["-question_added_datetime"]

    
    def __str__(self):
        return "self.name"