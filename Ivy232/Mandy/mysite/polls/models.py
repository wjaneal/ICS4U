import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200) # CharField for character fields
    pub_date = models.DateTimeField('date published') # DateTimeField for datetimes. 

    def __str__(self): # print the objects(questions).
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # ForeignKey tells Django each Choice is related to a single Question.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self): # print the objects(choices/answers).
        return self.choice_text

def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
