from django.conf.urls import url, include
from .views import all_reviews, LeaveReviewForm



urlpatterns = [
    url(r'^$', all_reviews, name='reviews'),
     url(r'^$', LeaveReviewForm, name='your-review'),
]