from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Room(models.Model):
    
    ROOM_CATEGORIES=(
        ('YAC','AC'), # (CODE , Display)
        ('NAC','NON-AC'),
        ('DEL','DELUXE'),
        ('KIN','KING'),
        ('QUE','QUEEN'),
    )

    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people' 

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    

    def __str__(self):
        return f'{self.user} has booked room {self.room.number} from {self.check_in} to {self.check_out}'
