from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import ProductReview
from .forms import ProductReviewForm
from products.models import Product
from profiles.models import UserProfile

from django.contrib.auth.decorators import login_required


@login_required
def add_review(request, product_id):
    """ Allow user to add review of products:
    view should only be limited to users who have bought the product"""

    product = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)

    # Check if user have purchased product:
    validated_purchase = False
    if product in profile.user_purchases.all():
        validated_purchase = True
    # Check if user has already reviewed:
    # https://stackoverflow.com/questions/38370908/how-to-check-if-a-user-already-likes-a-blog-post-or-not-in-django
    already_reviewed = ProductReview.objects.filter(
        user_profile=profile, product=product
    ).exists()
    if already_reviewed:
        messages.error(request, 'Sorry, you have already reviewed')
        return redirect(reverse('home'))
    if not validated_purchase:
        messages.error(
            request,
            'Sorry, only verified buyers can submit a review for this product'
        )
        return redirect(reverse('home'))
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ProductReviewForm(request.POST)
            if form.is_valid():
                # use of instance inspired by:
                # https://www.youtube.com/watch?v=zJWhizYFKP0
                instance = form.save(commit=False)
                instance.product = product
                instance.user_profile = profile
                instance.save()
                messages.success(request, 'Successfully added review')
                return redirect('product_detail', product_id)
            else:
                messages.error(
                    request,
                    'Failed to add review. Please ensure the form is valid.'
                )
    else:
        form = ProductReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_review(request, product_id, product_review_id):
    """ Allow user to add review of products:
    view should only be limited to users who have bought the product"""
    product_review = get_object_or_404(ProductReview, pk=product_review_id)
    product = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.user != product_review.user_profile.user:
        messages.error(request, 'Forbidden')
        return redirect('product_detail', product_id)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ProductReviewForm(request.POST, instance=product_review)
            if form.is_valid():
                # use of instance inspired by:
                # https://www.youtube.com/watch?v=zJWhizYFKP0
                instance = form.save(commit=False)
                instance.product = product
                instance.user_profile = profile
                instance.save()
                messages.success(request, 'Successfully updated review')
                return redirect('product_detail', product_id)
            else:
                messages.error(
                    request,
                    'Failed to update review. Please ensure the form is valid.'
                )
    else:
        form = ProductReviewForm(instance=product_review)
    template = 'reviews/edit_review.html'
    context = {
        'product': product,
        'review': product_review,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_review(request, product_id, product_review_id):
    """Allow users to delete a review"""
    product_review = get_object_or_404(ProductReview, pk=product_review_id)
    product = get_object_or_404(Product, pk=product_id)
    if product != product_review.product:
        messages.error(request, 'Wrong product')
        return redirect('product_detail', product_id)
    if request.user != product_review.user_profile.user:
        messages.error(request, 'Forbidden')
        return redirect('product_detail', product_id)
    if request.user.is_authenticated:
        product_review.delete()
        messages.success(request, 'Review deleted!')
    return redirect('product_detail', product_id)
