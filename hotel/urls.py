from django.urls import path
from .views import RoomListView, BookingList, BookingView, RoomDetailView
#app_name = 'hotel'

urlpatterns = [
    path('room_list/', RoomListView, name='room_list'),
    path('booking_list/', BookingList.as_view(), name='booking_list'),
    path('book/', BookingView.as_view(), name='booking_view'),
    path('room/<category>', RoomDetailView.as_view(), name='room_detail'),
]
