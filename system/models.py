from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Discipline(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()


    def __str__(self):
        return self.name


class Theme(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    info = models.TextField()


    def __str__(self):
        return self.name


class Test(models.Model):
    theme = models.ForeignKey(Theme ,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    info = models.TextField()
    bal = models.FloatField(default = 0)
    publish_data = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.name


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None, blank = True)
    complexity = models.IntegerField()
    right_choice = models.CharField(max_length=10)


    def __str__(self):
        return self.text


class Choice(models.Model):
    number = models.IntegerField(help_text='enter number of choice')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField( max_length=300)


class InfoUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    count = models.FloatField()
    bal = models.IntegerField(default=2)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)



