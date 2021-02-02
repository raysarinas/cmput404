from django.db import models

# Create your models here.
# tell Django here what we want so that it translates code (Python objects) 
# into SQL code and create the tables for us
# Django will make the tables for us and figure out the details of it and stuff

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)