from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    ue = UpcomingEvent.objects.order_by('event_date')
    f  = fact.objects.order_by('-fact_no')[:4]
    context = {  
        'upcoming_events': ue,
        'facts': f
      }
    return render(request, 'home.html', context)

def about(request):
    a = aboutUS.objects.order_by('showing_order')
    rules = Rules.objects.order_by('rule_no')
    context = {
        "rules": rules,
        'about': a
    }
    return render(request, 'about.html', context)

def activity(request):
    e = events.objects.order_by('-date')
    i = eventPhoto.objects.order_by('-event_date')
    
    context = {
        'i': i,
        'e': e
    }
    return render(request, 'activity.html', context)

def gallery(request):
    g = Gallery.objects.order_by('-event_date')
    e = []
    for i in g:
        if i.event_date not in e:
            e.append(i.event_date)
    
    context = {
        'g': g,
        'e': e,
    }
    return render(request, 'gallery.html', context)

def contact(request):
    fc = FounderContact.objects.all()
    lp = Contact.objects.filter(pos='lp')
    a = Contact.objects.filter(pos='a')
    p = Contact.objects.filter(pos='p')
    context = {
        'fc': fc,
        'lp': lp,
        'a' : a,
        'p' : p
    }
    return render(request, 'contact.html', context)

def dev(request):
    context = {}
    return render(request, 'dev.html', context)


def downloads(request):
    b = Brochure.objects.order_by('-date')[0]
    context = {
        'brochure': b
      }
    return render(request, 'downloads.html', context)

def test(request):
    e = events.objects.order_by('-date')
    i = eventPhoto.objects.order_by('-event_date')
    
    context = {
        'i': i,
        'e': e
    }
    return render(request, 'test.html', context)

def facts(request):
    f = fact.objects.order_by('-fact_no')
    context = {
        'facts': f
    }
    return render(request, 'facts.html', context)