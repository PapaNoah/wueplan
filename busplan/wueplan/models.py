from django.db import models

class Station(models.Model):
  name = models.CharField(max_length=250)
  
  def __unicode__(self):
    return self.name
  
class Lines(models.Model):
  name = models.CharField(max_length=250)
  station = models.ManyToManyField(Station)
  startstation = models.ForeignKey(Station, related_name='lines_startstation')
  endstation = models.ForeignKey(Station, related_name='lines_endstation')
  
  def __unicode__(self):
    return self.name

class Times(models.Model):
  NORMAL = 'NO'
  SATURDAY = 'SA'
  SUNDAY = 'SU'
  
  DAY = (
    (NORMAL, 'Normal'),
    (SATURDAY, 'Samstag'),
    (SUNDAY, 'Sonntag/Feiertag'),
  )
  
  time = models.TimeField()
  station = models.ForeignKey(Station)
  lines = models.ForeignKey(Lines)
  day = models.CharField(max_length=2,choices=DAY)
  
  
  def __unicode__(self):
    return str(self.time)