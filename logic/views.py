from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import EventsAndTours, contactUs
from django.utils import timezone
from django.urls import reverse
import feedparser

# Create your views here.
def index(request):
    channel_id = 'UCUkxt42zDNYFPa7S8_j4phg'
    rss_feed = 'https://www.youtube.com/feeds/videos.xml?channel_id='+channel_id
    futureEvents, pastEvents = getEvents()

    context = {'ChannelData':getDataFromChannel(rss_feed), 'futureEvents': futureEvents, 'pastEvents': pastEvents}

    return render(request, 'logic/full.html',context=context)

def getDataFromChannel(url,slides=5):
    youtube_feed = feedparser.parse(url)
    entry = youtube_feed.entries[:slides]
    return entry

def getEvents(howMany=3):
    events = EventsAndTours.objects.all()
    futureEvents = events.exclude(date__lt=timezone.now()).order_by('-date').reverse()[:howMany]
    pastEvents = events.exclude(date__gt=timezone.now()).order_by('-date')[:howMany]
    return futureEvents, pastEvents

def contactForm(request):
    name = request.POST['Name']
    contact = request.POST['contact']
    message = request.POST['Message']

    contactUs.objects.create(name=name,contact=contact,message=message)

    return HttpResponseRedirect(reverse('logic:home'))
