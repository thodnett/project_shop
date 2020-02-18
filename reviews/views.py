from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Review
from django.urls import reverse
from .forms import LeaveReviewForm
# Create your views here.


# Create your views here.
 
def all_reviews(request):
    reviews = Review.objects.all()
    return render(request, "reviews.html", {"reviews": reviews})
    

def LeaveReviewForm(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LeaveReviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
           LeaveReviewForm.save()

 
    else:
        form = LeaveReviewForm(request)

    return render(request, 'leavereview.html', {'form': form})