from django.db import models
# from django.db.models.expressions import F
# from django.db.models.fields.files import ImageField

# Create your models here.


class tourModel(models.Model):
    title = models.CharField(max_length=100, blank=False)
    date = models.DateField(auto_now_add=False)
    image = models.ImageField(upload_to="images/pics")
    details = models.TextField(blank=False)

    def __str__(self):
        return self.title


class feedbackModel(models.Model):
    name = models.CharField(max_length=50, blank=False)
    tweethandl = models.CharField(max_length=50)
    tweet = models.TextField()

    def __str__(self):
        return self.name
