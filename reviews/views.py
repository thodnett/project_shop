
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Review
from .forms import LeaveReviewForm
# Create your views here.


# Create your views here.
 
def all_reviews(request):
    reviews = Review.objects.all()
    return render(request, "reviews.html", {"reviews": reviews})
    

def leave_review(self, request, pk):
    review_instance = get_object_or_404(ReviewInstance, pk=pk)


    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = LeaveReviewForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            review_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all_reviews') )

    context = {
        'form': form,
        'review_instance': review_instance,
    }

    return render(request, 'leavereview.html', context)