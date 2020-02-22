from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.index, name='poll_index'),
	path('book/<int:room_id>', views.bookScreen,
	 name='book_screen')
]