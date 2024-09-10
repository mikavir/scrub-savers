from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import ProductReview
from .forms import ProductReviewForm
from products.views import product_detail
from products.models import Product
from profiles.models import UserProfile

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def add_review(request, product_id):
    """ Allow user to add review of products: view should only be limited to users who have bought the product"""
    product = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ProductReviewForm(request.POST)
            if form.is_valid():
                # use of instance inspired by: https://www.youtube.com/watch?v=zJWhizYFKP0
                instance=form.save(commit=False)
                instance.product=product
                instance.user_profile = profile
                instance.save()
                messages.success(request, 'Successfully added review')
                return redirect('product_detail', product_id)
            else:
                messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = ProductReviewForm()
        
    template = 'reviews/add_review.html'
    context = {
        'product': product,
        'form': form,
    }

    return render(request, template , context)
