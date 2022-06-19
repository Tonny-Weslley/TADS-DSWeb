from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('de publicação')

    def __str__(self):
        return ("{0} - {1}").format(self.id, self.question_text)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField('Quantidade de votos', default=0)

    def __str__(self):
        return ("{0} - {1}").format(self.question.question_text, self.choice_text)
