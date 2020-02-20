from django.conf.urls import url, include
from .views import all_reviews, leave_review



urlpatterns = [
    url(r'^$', all_reviews, name='reviews'),
    url(r'^leave_review/(?P<pk>\d+)/$', leave_review, name='leave_review')
]