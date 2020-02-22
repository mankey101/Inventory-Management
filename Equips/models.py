from django.db import models
from django.utils.timezone import now
# Create your models here.


class Equipment(models.Model):
    index = models.IntegerField(primary_key=True)
    equip_type = models.CharField(max_length=200)
    actual_equipment = models.CharField(max_length=100)
    status = models.CharField(max_length=1, default='+')
    issued_to = models.CharField(max_length=50, blank=True, null=True)
    lastIssued = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.equip_type + "_" + self.actual_equipment + "_" + str(self.index)


#
# class Room(models.Model):
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
