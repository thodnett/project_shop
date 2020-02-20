from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Review
from django.contrib.auth.models import User
from .forms import LeaveReviewForm
# Create your views here.


# Create your views here.
 
def all_reviews(request):
    reviews = Review.objects.all()
    return render(request, "reviews.html", {"reviews": reviews})
    

def leave_review(request):
     user = User.objects.first() 
     form = LeaveReviewForm()
     if request == 'POST':
         form = LeaveReviewForm(request.POST)
         if form.is_valid():
             review = form.save()
             return redirect('all_reviews')
         else:
             form = LeaveReviewForm()
     return render(request, 'leavereview.html', {'form': form})
         
