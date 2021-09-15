import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class EventsAndTours(models.Model):
    eventName = models.TextField(max_length=200)
    date = models.DateTimeField('Event Date')
    district = models.TextField(max_length=100, default='Surendranagar')
    address = models.TextField(max_length=1000)
    about = models.TextField(max_length=1000)
    location = models.TextField(max_length=1000)

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.eventName + str(self.date)

class contactUs(models.Model):
    name = models.TextField(max_length=50)
    contact = models.TextField(max_length=100)
    message = models.TextField(max_length=200)

    def __str__(self):
        return "Name: {} \n Message: {} \n Contact: {}".format(self.name, self.message, self.contact)