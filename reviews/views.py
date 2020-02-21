from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Review
from products.models import Product
from django.contrib.auth.models import User
from .forms import LeaveReviewForm
# Create your views here.


# Create your views here.
 
def all_reviews(request):
    reviews = Review.objects.all()
    return render(request, "reviews.html", {"reviews": reviews})
    

def leave_review(request, id):
    
     form = LeaveReviewForm()
     product = get_object_or_404(Product, pk=id)
     if request.method == 'POST':
        form = LeaveReviewForm(request.POST)
  
  
        if form.is_valid():
            review = form.save(commit= False)
            review.user_name = request.user
            review.product_name = product
            review.save()
        return redirect('all_reviews')
             
     else:
             form = LeaveReviewForm()
     return render(request, 'leavereview.html', {'form': form, id : id})
         
