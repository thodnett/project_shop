from reviews.models import Review
from django import forms 


class LeaveReviewForm(forms.Form):
    
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
   

    product_name = forms.CharField(max_length=100)
    user_name = forms.CharField(max_length=100)
    comment = forms.CharField(max_length=200)
    rating = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=RATING_CHOICES,
    )
    

