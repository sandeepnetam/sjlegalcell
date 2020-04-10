from django.db import models
from django.db.models.signals import post_delete
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
    )
    name   = models.CharField( max_length=100)
    mobile = models.CharField( max_length=10)
    desgn  = models.ForeignKey(Designation, on_delete=models.CASCADE)
    pos    = models.CharField( max_length=100, choices=POS_CHOICES, default='p')
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