from django.conf.urls import url
from . import views

urlpatterns = [


	# list all the reviews in the applications
	url(r'^$', views.review_list, name="review_list"),
	
	# detailing all the information about the reviews
	url(r'^reviews/(?P<review_id>[0-9]+)/$', views.review_detail, name="review_detail"),

	# listing all the wine here
	url(r'^wine$', views.wine_list, name="wine_list"),

	# the details of the reviews
	url(r'^wine/(?P<wine_id>[0-9]+)/$', views.wine_detail, name="wine_detail"),
	url(r'^wine/(?P<wine_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),

	# ex: /review/user/ - get reviews for the logged user

	url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
	url(r'^review/user/$', views.user_review_list, name='user_review_list'),

	# On loading more services to one page and filter them

	url(r'^all_services$', views.all_services, name="all_services"),

	#url(r'^category/(?P<wine_id>[0-9]+)/$', views.business_category, name='business_category'),
]