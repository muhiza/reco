from django.shortcuts import get_object_or_404, render
from .models import Review, Wine
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import ReviewForm
import datetime
# On users management issues

from django.contrib.auth.decorators import login_required

def review_list(request):
	latest_review_list = Review.objects.order_by('-pub_date')[:30]
	context  = {'latest_review_list': latest_review_list}
	return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
	review = get_object_or_404(Review, pk=review_id)
	return render(request, 'reviews/review_detail.html', {'review':review})


def wine_list(request):
	wine_list_view = Wine.objects.order_by('-time')[:6]
	context = {'wine_list_view': wine_list_view}

	query = request.GET.get("q")
	if query:
		wine_list_view = wine_list_view.filter(title__icontains=query) 


	return render(request, 'reviews/index.html', context)


def all_services(request):
	all_list_view = Wine.objects.order_by('-time')[:100]
	context = {'all_list_view': all_list_view}
	return render(request, 'reviews/all_services.html', context)




def wine_detail(request, wine_id):
	wine = get_object_or_404(Wine, pk=wine_id)
	return render(request, 'reviews/wine_detail.html', {'wine': wine})

@login_required
def add_review(request, wine_id):
	wine = get_object_or_404(Wine, pk=wine_id)
	form = ReviewForm(request.POST)
	if form.is_valid():
		rating    = form.cleaned_data['rating']
		comment   = form.cleaned_data['comment']
		user_name = request.user.username
		
		review = Review()
		review.wine   = wine
		review.user_name = user_name
		review.rating    = rating
		review.comment   = comment
		review.pub_date  = datetime.datetime.now()
		review.save()

		return HttpResponseRedirect(reverse('reviews:wine_detail', args=(wine.id,)))

	return render(request, 'reviews/wine_detail.html', {'wine': wine, 'form': form})


def user_review_list(request, username=None):
    if not username:
        username = request.user.username
    latest_review_list = Review.objects.filter(user_name=username).order_by('-pub_date')
    context = {'latest_review_list':latest_review_list, 'username':username}
    return render(request, 'reviews/user_review_list.html', context)



def related_products(request):
	related = Wine.objects.filter


"""
def business_category(request, wine_id):
	business_category_list = Wine.objects.filter(wine_type="red", pk=wine_id)
	context = {"business_category_list": business_category_list }
	return render(request, 'reviews/business_category.html', context)

"""