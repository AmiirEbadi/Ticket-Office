from django.db import models
from stadium.models import Stadium
 
# Create your models here.

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='team_logo', blank=True, null=True)
    
    def __str__(self):
        return self.name

    
class Match(models.Model):
    team1 = models.ForeignKey(Team, null=False, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    time = models.DateTimeField()
    
    def __str__(self):
        return self.team1.name + ' vs ' + self.team2.name


