from django.urls import path
from .views import TeamViewSet, MatchViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [

]

router = DefaultRouter()
router.register(r'team', TeamViewSet, basename='team')
router.register(r'', MatchViewSet, basename='match')
urlpatterns += router.urls