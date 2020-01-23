from django.conf.urls import url, include
from .views import all_reviews

urlpatterns = [
    url(r'^$', all_reviews, name='reviews'),
]