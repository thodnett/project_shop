from django import forms
from .models import Review 
from products.models import Product


class LeaveReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['comment', 'rating']
        