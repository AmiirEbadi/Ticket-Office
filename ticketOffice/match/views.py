from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import (
    ListCreateAPIView,
)
from .permissions import IsAdminOrReadOnly
from .serializers import TeamSerializer, MatchSerializer
from .models import Team, Match


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    

class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
    permission_classes = [IsAdminOrReadOnly]