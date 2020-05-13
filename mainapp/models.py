from django.db import models
from django.db.models.signals import post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.

class events(models.Model):
    name  = models.CharField(max_length=100)
    date  = models.DateField(auto_now=False, auto_now_add=False)
    descr = models.TextField(max_length=None)

    def __str__(self):
        return self.date.strftime("%d-%m-%Y")

class eventPhoto(models.Model):
    event_date = models.ForeignKey(events, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='events/')

    def __str__(self):
        return str(self.id)
@receiver(post_delete, sender=eventPhoto)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

class Rules(models.Model):
    id      = models.AutoField(primary_key = True, null=False)
    rule_no = models.IntegerField(default=0)
    rule    = models.TextField(max_length=1000)
    rule_en = models.TextField(max_length=1000)

    def __str__(self):
        return  f"Rule {self.rule_no} --> {self.rule}"

class Gallery(models.Model):
    event_date = models.ForeignKey(events, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="gallery")

    def __str__(self):
        return str(self.id)
    
@receiver(post_delete, sender=Gallery)
def submission_delete(sender, instance, **kwargs):
    instance.img.delete(False) 

class Designation(models.Model):
    desgn = models.CharField( max_length=100)

    def __str__(self):
        return str(self.desgn)

class Contact(models.Model):
    POS_CHOICES = (
        ('lp','Legal Panel/Advisor'),
        ('p', "Patron"),
        ('a', "Advocate"),
        ('m', "Active Member"),
    )
    state_choice = (
        ('', ''),
        ('ap', "Andra Pradesh"),
        ('arp', "Arunachal Pradesh"),
        ('a', "Assam"),
        ('b', "Bihar"),
        ('cg', "Chhattisgarh"),
        ('goa', "Goa"),
        ('g', "Gujarat"),
        ('h', "Haryana"),
        ('hp', "Himachal Pradesh"),
        ('jk', "Jammu and Kashmir"),
        ('j', "Jharkhand"),
        ('k', "Karnataka"),
        ('kr', "Kerala"),
        ('mp', "Madya Pradesh"),
        ('m', "Maharashtra"),
        ('mani', "Manipur"),
        ('meg', "Meghalaya"),
        ('miz', "Mizoram"),
        ('ng', "Nagaland"),
        ('o', "Orissa"),
        ('pun', "Punjab"),
        ('raj', "Rajasthan"),
        ('s', "Sikkim"),
        ('tn', "Tamil Nadu"),
        ('t', "Telagana"),
        ('tp', "Tripura"),
        ('u', "Uttaranchal"),
        ('up', "Uttar Pradesh"),
        ('wb', "West Bengal"),
        ('an', "Andaman and Nicobar Islands"),
        ('c', "Chandigarh"),
        ('dn', "Dadar and Nagar Haveli"),
        ('dd', "Daman and Diu"),
        ('del', "Delhi"),
        ('l', "Lakshadeep"),
        ('pu', "Puducherry"),
    )
    name   = models.CharField( max_length=100)
    mobile = models.CharField( max_length=10)
    desgn  = models.ForeignKey(Designation, on_delete=models.CASCADE)
    state  = models.CharField("State", max_length=60, choices=state_choice, default='')
    pos    = models.CharField( max_length=100, choices=POS_CHOICES, default='m')
    show   = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

class FounderContact(models.Model):
    name   = models.CharField( max_length=100)
    mobile = models.CharField( max_length=10)
    desgn  = models.ForeignKey(Designation, on_delete=models.CASCADE)
    img    = models.ImageField(upload_to='FoundersContactImages')
    show   = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)
@receiver(post_delete, sender=FounderContact)
def submission_delete(sender, instance, **kwargs):
    instance.img.delete(False) 

class UpcomingEvent(models.Model):
    event_name  = models.CharField(max_length=100)
    event_date  = models.DateField(auto_now=False, auto_now_add=False)
    event_descr = models.TextField(max_length=None)

    def __str__(self):
        return str(self.event_name)


class Brochure(models.Model):
    b = models.FileField(upload_to='brochure', name='SJLC_Brochure')
    date  = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'SJLC Brochure : {self.date.strftime("%d-%m-%Y")}'
    
@receiver(post_delete, sender=Brochure)
def submission_delete(sender, instance, **kwargs):
    instance.SJLC_Brochure.delete(False) 


class fact(models.Model):
    id = models.AutoField(primary_key=True)
    fact_no = models.IntegerField(unique=True, auto_created=True)
    fact = models.TextField(unique=True)

    def __str__(self):
        return f"{self.fact_no} : {self.fact}"

class aboutUS(models.Model):
    heading = models.CharField(max_length=100)
    detail = models.TextField(default='', editable=True, blank=True)
    detail_en = models.TextField(default='', editable=True, blank=True)
    showing_order = models.IntegerField()

    def __str__(self):
        return f"{self.showing_order} : {self.heading} --> {self.detail}"

class account_info(models.Model):
    acc_no = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=100)
    bank_name = models.CharField( max_length=100)

    def __str__(self):
        return self.acc_no



##########################################  MIS  ###############################################################
class District(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class MIS(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User Name') # User Releted
    name = models.CharField(max_length = 150)
    guardian_name = models.CharField(max_length = 150)
    married = models.BooleanField(default=False)
    date_of_birth = models.CharField(max_length=10,help_text="Format : yyyy-mm-dd")
    GENDER = (
        ('',''),
        ('F','Female'),
        ('M','Male'),
        ('O','Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDER, default='')
    CATEGORY = (
        ('',''),
        ('SC', 'Schedule Caste'),
        ('ST', 'Schedule Tribe'),
        ('OBC', 'Other Backward Class'),
        ('Min', 'Minorities'),
    )
    category = models.CharField(max_length=5, choices=CATEGORY, default='')
    caste    = models.CharField(max_length = 20)
    age      = models.IntegerField()
    mobile      = models.CharField(max_length = 10)
    QUALIFICATION =(
        ('',''),
        ('S', 'STUDENT'),
        ('UG', 'UNDERGRADUATE'),
        ('G', 'GRADUATE'),
        ('PG', 'POSTGRADUATE'),
        ('PhD', 'PhD'),
        ('MP', 'M.Phil'),
        ('P', 'PROFESSIONAL'),
        ('BM', 'BUSINESSMAN'),
        ('O', 'OTHER'),
    )
    qualification = models.CharField(max_length=60, choices=QUALIFICATION, default='')
    department  = models.ForeignKey(Department, on_delete=models.PROTECT)
    date_of_joining_in_depart = models.CharField(max_length=10)
    post = models.CharField(max_length = 100)
    CLASS = (
        ('',''),
        ('I'  ,'Class I'),
        ('II' ,'Class II'),
        ('III','Class III'),
        ('IV' ,'Class IV'),
    )
    Class       = models.CharField(max_length = 5, choices=CLASS, default='')
    promotion_date =models.CharField(max_length=10, blank=True)
    district    = models.ForeignKey(District, on_delete=models.PROTECT)
    block       = models.CharField(max_length = 100)
    postal_addr = models.TextField(max_length = 300, blank=True)
    permanent_addr = models.TextField(max_length = 300, blank=True)
    pincode     = models.CharField(max_length = 6)
    accepted    = models.BooleanField(default=False)

    def __str__(self):
        return self.name
