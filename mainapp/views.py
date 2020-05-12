from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    ue = UpcomingEvent.objects.order_by('event_date')
    f  = fact.objects.order_by('-fact_no')[:4]
    a_info = account_info.objects.all()
    if len(list(a_info)) != 0:
        a_info = a_info[0]
    context = {  
        'upcoming_events': ue,
        'facts': f,
        'a_info': a_info
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
    b = Brochure.objects.order_by('date')
    if len(list(b)) != 0:
        b = b[0]
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

def mis_indi(request, pk):
    context = {
        'person': MIS.objects.get(id=pk)
    }
    return render(request, 'mis_individual.html', context)

def mis_list(request):
    context = {
        'mis': MIS.objects.all()
    }
    return render(request, 'mis_list.html', context)

def mis_success(request):
    context = {}
    return render(request, "mis_success.html", context)

def mis(request):
    context = {
        'error': False,
        'error_msgs': '',
        'departments': Department.objects.all(),
        'districts': District.objects.all()
    }
    if request.method == "POST":
        print (request.POST)
        if request.POST['name']and request.POST['g_name'] and request.POST['dob'] and request.POST['gender'] and request.POST['age'] and request.POST['mobile'] and request.POST['per_addr'] and request.POST['pincode'] and request.POST['department'] and request.POST['doj'] and request.POST['post'] and request.POST['class'] and request.POST['district'] and request.POST['block'] and request.POST['postal_addr']:
            error_msgs = []
            name       = request.POST['name']
            g_name     = request.POST['g_name']
            dob        = request.POST['dob']
            gender     = request.POST['gender']
            age        = request.POST['age']
            mobile     = request.POST['mobile']
            try:
                married = True if request.POST['married'] == 'on' else False
            except:
                married = False
            category   = request.POST['category']
            caste      = request.POST['caste']
            per_addr   = request.POST['per_addr']
            pincode    = request.POST['pincode']
            department = request.POST['department']
            doj        = request.POST['doj']
            post       = request.POST['post']
            Class      = request.POST['class']
            qualification  = request.POST['qualification']
            promotion_date = request.POST['promotion_date'] if request.POST['promotion_date'] else ''
            district       = request.POST['district']
            block          = request.POST['block']
            postal_addr    = request.POST['postal_addr']
            
            
            if (1 <= len(mobile) < 10) or (len(mobile) > 10):
                error_msg = "Mobile number must be of 10 characters."
                error_msgs.append(error_msg)
                context['error'] = True
                context['error_msgs'] = error_msgs

            if 5 < len(pincode) > 6:
                error_msg = "Invalid pincode."
                error_msgs.append(error_msg)
                context['error'] = True
                context['error_msgs'] = error_msgs

            if age:
                print(f"Age : {age}")
                if int(age) <= 18:
                    error_msg = "Inavalid age."
                    error_msgs.append(error_msg)
                    context['error'] = True
                    context['error_msgs'] = error_msgs
                #error_msg = "Mobile number must be of 10 characters."
                #error_msgs.append(error_msg)
                #context['error'] = True
                #context['error_msgs'] = error_msgs
            else:
                error_msg = "Input Age."
                error_msgs.append(error_msg)
                context['error'] = True
                context['error_msgs'] = error_msgs
            
            if not ''.join(name.split(' ')).isalpha():
                error_msg = "Name must only contain alphabets."
                error_msgs.append(error_msg)
                context['error'] = True
                context['error_msgs'] = error_msgs

            if not ''.join(g_name.split(' ')).isalpha():
                error_msg = "Father/husband name must only contain alphabets."
                error_msgs.append(error_msg)
                context['error'] = True
                context['error_msgs'] = error_msgs
            
            if department == '0':
                error_msg = "Please select one department."
                error_msgs.append(error_msg)
                context['error'] = True
                context['error_msgs'] = error_msgs
            
            if gender == '0':
                error_msg = "Please select your gender."
                error_msgs.append(error_msg)
                context['error'] = True
                context['error_msgs'] = error_msgs

            if Class == '0':
                error_msg = "Please select your Class."
                error_msgs.append(error_msg)
                context['error'] = True
                context['error_msgs'] = error_msgs

            if qualification == '0':
                error_msg = "Please select your qualification."
                error_msgs.append(error_msg)
                context['error'] = True
                context['error_msgs'] = error_msgs

            if district == '0':
                error_msg = "Please select your district."
                error_msgs.append(error_msg)
                context['error'] = True
                context['error_msgs'] = error_msgs

            if context['error']:
                return render(request, 'mis.html', context)
            else:
                m = MIS()
                m.name = name
                m.guardian_name = g_name
                m.date_of_birth = dob
                m.gender = gender
                m.age = age
                m.mobile = mobile
                m.married = married
                m.category = category
                m.caste = caste
                m.qualification = qualification
                m.permanent_addr = per_addr
                m.pincode = pincode
                m.department = Department.objects.get(name=department)
                m.date_of_joining_in_depart = doj
                m.post = post
                m.Class = Class
                if promotion_date:
                    m.promotion_date = promotion_date
                m.district = District.objects.get(name=district)
                m.block = block
                m.postal_addr = postal_addr
                m.save()
                context = {
                    'submitted_success' : True
                }
                return redirect(mis_success)
        else:
            context['error'] = True
            context['error_msgs'] = ['Some fields are empty.']
            return render(request, 'mis.html', context)

    return render(request, 'mis.html', context)