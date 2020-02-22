from django.db import models

# Create your models here.

class RoomResource(models.Model):
	s_no = models.CharField('Ref No.',max_length = 10)
	# name
	desc = models.CharField(max_length = 100)
	#location
	location = models.CharField(max_length = 100)

	def __str__(self):
		return self.desc

# Can be accessed in RoomResource by using command 
# RoomResource.roombooking_set object!
class RoomBooking(models.Model):
	room = models.ForeignKey(RoomResource, on_delete = models.CASCADE, null=False )
	start_time = models.DateTimeField('Start of booking', null=False)
	end_time = models.DateTimeField('End of Booking', null = False)

	def __str__(self):
		return self.room.desc
