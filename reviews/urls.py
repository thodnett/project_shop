from django.conf.urls import url, include
from .views import all_reviews, leave_reviewform


urlpatterns = [
    url(r'^$', all_reviews, name='reviews'),
    url(r'^leave_reviewform/(?P<id>\d+)/', leave_reviewform, name='leave_reviewform')
  
   
   
]