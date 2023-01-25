from rest_framework import serializers
from .models import Team, Match


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
     
        
class MatchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Match
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['team1'] = TeamSerializer(instance.team1).data
        data['team2'] = TeamSerializer(instance.team2).data
        return data
