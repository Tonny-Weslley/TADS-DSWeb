from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Data de publicação')
    def __str__(self):
        return str(self.id) + ' : ' + self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return 'Opção: ' + self.choice_text +" - \nReferente a pergunta: " + self.question.question_text