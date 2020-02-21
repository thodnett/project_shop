from django import forms
from .models import Review


class LeaveReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = [ 'comment', 'rating']
