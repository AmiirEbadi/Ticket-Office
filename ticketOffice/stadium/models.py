from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class Stadium(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    
    def capacity(self):
        return sum([section.remain_count() for section in self.section_set.all()])
    
    def __str__(self):
        return self.name


class Section(models.Model):
    section_number = models.CharField(max_length=30)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    
    def remain_count(self):
        remain_seats_count =  self.capacity - self.seat_set.filter(reserved=True).count()
        return remain_seats_count
    
    def __str__(self):
        return self.section_number


    
class Seat(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    reserved = models.BooleanField(default=False)
    seat_number = models.CharField(max_length=30)
    
    def __str__(self):
        return self.seat_number