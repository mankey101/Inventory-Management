# https://docs.djangoproject.com/en/3.0/topics/db/queries/
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader
from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from datetime import datetime, timedelta, tzinfo
from django.urls import reverse

from .models import RoomResource, RoomBooking

# Create your views here.
def index(request):
	all_rooms_list = RoomResource.objects.order_by('id')


	context = {
		'all_rooms_list': all_rooms_list,
		'head_title': 'Rooms!'
	}

	return render(request, 'polls/index.html', context)

# need a room as context. 
def bookScreen(request, room_id):
	room = get_object_or_404(RoomResource, id=room_id)
	errormsg = None
	try:
		req_rno = request.POST['rno']
		req_stt = request.POST['start_tm']
	# see if post values are there. If not, render 
	# basic page
	except:
		req_rno = None
		return render(request, 'polls/book.html', 
		{'room':room, 'head_title':'Room Book'})
	else:
		try:
			begin = parse_datetime(req_stt)
		except:
			errormsg = "Enter Valid DateTime!"	
			return render(request, 'polls/book.html', 
			{'room':room, 'head_title':'Room Book', 
			'errormsg': errormsg})
		else:
			if(begin is None):
				errormsg = "Enter Valid DateTime!"	
				return render(request, 'polls/book.html', 
				{'room':room, 'head_title':'Room Book', 
				 'errormsg': errormsg})			
			else:
				end = begin + timedelta(minutes=59)
				thisbook = RoomBooking(room=room, start_time=begin, end_time=end, roll_no=req_rno)
				# thisbook.save()
				# Do it later after some checks
				
				# room_id === foreign-key.id
				querySet = RoomBooking.objects.filter(room_id = room.id).filter(
						end_time__gte=thisbook.start_time,
						start_time__lte=thisbook.end_time,
						active__exact=True,
					)

				if querySet.count()==0:
					thisbook.save()
					return render(request, 'polls/book.html', 
					{'room':room, 'head_title':'Room Book', 
					'booking_info': thisbook})
				else:
					return render(request, 'polls/book.html', 
					{'room':room, 'head_title':'Room Book', 
				 	'errormsg': 'This slot is already booked!'})	

def clearAllBookings(request):
	RoomBooking.objects.all().delete()
	return HttpResponse('Deleted all. ')

def allBookings(request):
	all_rooms_list = RoomBooking.objects.filter(active__exact=True, end_time__gte=datetime.now()).order_by('-start_time')

	context = {
		'all_rooms_list': all_rooms_list,
		'head_title': 'Rooms Bookings'
	}

	return render(request, 'polls/allBookings.html', context)

def cancelBooking(request, booking_id):
	booking = get_object_or_404(RoomBooking, id=booking_id)
	
	if (request.user.is_authenticated and request.user.email == booking.roll_no):
		booking.active=False
		booking.save()

	return HttpResponseRedirect(reverse('polls:allBookings'))