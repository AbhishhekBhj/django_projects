from django.db import models


# Create your models here.
class Contact(models.Model):
    # data for model class
    email = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    date = models.DateField()
    desc = models.TextField()

    # save contact by the name
    def __str__(self):
        return self.name
