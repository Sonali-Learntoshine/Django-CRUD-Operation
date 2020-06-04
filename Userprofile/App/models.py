from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='media')
    marks = models.IntegerField(default=0)
    caption = models.TextField(max_length=500)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    dob = models.DateField()
    designation = models.CharField(max_length=30)

    def __str__(self):
        return self.name