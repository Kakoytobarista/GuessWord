from django.urls import include, path
from rest_framework import routers

from api.views import LinkViewSet


router = routers.DefaultRouter()
router.register('links', LinkViewSet, basename='links')


urlpatterns = (
    path('', include(router.urls)),
)
