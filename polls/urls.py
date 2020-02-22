from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.index, name='poll_index'),
	path('book/<int:room_id>', views.bookScreen,
	 name='book_screen'),
	path('deleteAll', views.clearAllBookings, name='clrAllBookings'),
	path('book/all', views.allBookings, name="allBookings"),
	path('book/cancel/<int:booking_id>', views.cancelBooking, name="cancelBooking")
]