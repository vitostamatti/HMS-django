from django.urls import path
from .views import RoomListView, BookingList, RoomDetailView, CancelBookingView
#app_name = 'hotel'

urlpatterns = [
    path('room_list/', RoomListView, name='room_list'),
    path('booking_list/', BookingList.as_view(), name='booking_list'),
    path('room/<category>', RoomDetailView.as_view(), name='room_detail'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(),
         name='cancel_booking_view'),
]
