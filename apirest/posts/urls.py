from django.conf.urls import include, url
from rest_framework import routers

from .views import PostViewset

api_router = routers.SimpleRouter()
api_router.register(r'posts', PostViewset, base_name='post')

urlpatterns = [
    url(r'', include(api_router.urls))
]
