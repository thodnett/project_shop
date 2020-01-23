from django.contrib import admin
from .models import Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('product_name','rating', 'user_name', 'comment')
    list_filter = ['rating', 'user_name']
    search_fields = ['comment']
    
admin.site.register(Review, ReviewAdmin)
