from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.template import loader
from django.shortcuts import render

from .models import RoomResource

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

	return render(request, 'polls/book.html', 
		{'room':room})
