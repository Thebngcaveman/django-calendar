from django.db import models

"""class Venue(models.Model):
    name = models.CharField('Venue Name',max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code',max_length=15)
    phone = models.CharField('Contact Phone',max_length=25)
    web = models.URLField('Website Address')
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.name

class CavemanClub(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name+ ' '+ self.last_name
    

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, blank=true,null)
    #venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=50)
    description = models.TextField(blank=true)
    attendees = models.ManyToManyField(CavemanClub,blank=true)

    def __str__(self):
        return self.name
"""