from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Review, Product
from products.models import Product
from django.contrib.auth.models import User
from .forms import LeaveReviewForm
# Create your views here.


# Create your views here.
 
def all_reviews(request):
    reviews = Review.objects.all()
    return render(request, "reviews.html", {"reviews": reviews})
    
def leave_review(request):
    products = Product.objects.all()
    return render(request, "leavereview.html", {"products": products})

def leave_reviewform(request, product_id):

     form = LeaveReviewForm()
     product = get_object_or_404(Product, product_id)
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
             context = {'product_id' : product_id}
     return render(request, 'leavereviewform.html', {'form': form}, context)
         
