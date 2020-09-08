from django.shortcuts import render, HttpResponse, reverse

from django.views.generic import ListView, FormView, View

from .forms import AvailabilityForm
from .models import *
from .booking_functions.availability import check_availability


def RoomListView(request):
    rooms = Room.objects.all()
    categories = dict(Room.ROOM_CATEGORIES)
    categories_values = categories.values()
    room_list = []
    for category in categories:
        room_category = categories.get(category)
        room_url = reverse('room_detail', kwargs={
            'category': category,
        })
        print(room_url)
        room_list.append((room_category, room_url))
    context = {
        'room_list': room_list,
    }
    return render(request, 'hotel/room_list.html', context)


class BookingList(ListView):
    model = Booking

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            book_list = Booking.objects.all()
            return book_list
        else:
            book_list = Booking.objects.filter(user=self.request.user)
            return book_list


class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForm
        room_list = Room.objects.filter(category=category)
        if len(room_list) > 0:
            room = room_list[0]
            room_category = dict(room.ROOM_CATEGORIES).get(room.category, None)
            context = {
                'category': room_category,
                'form': form,
                'room': room
            }
            return render(self.request, 'hotel/room_detail.html', context)
        else:
            return HttpResponse('Category does not exist')

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=category)
        form = AvailabilityForm(self.request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out'],
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All of this category of rooms are booked. Try another one or change date')


class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'hotel/room_detail.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out'],
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All of this category of rooms are booked. Try another one or change date')
