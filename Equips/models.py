from django.db import models
from django.utils.timezone import now
# Create your models here.

class Equipment(models.Model):
    index = models.IntegerField(primary_key=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    status = models.CharField(max_length=1, default='+')
    issued_to = models.TextField(default='', max_length=10)
    lastIssued = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.choice_text + "_" + str(self.index)


#
# class Room(models.Model):
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)