from django.contrib import admin
from .models import *

class ReviewAdmin(admin.ModelAdmin):
	model = Review
	list_display = ('wine', 'rating', 'user_name', 'comment', 'pub_date')
	list_filter = ['user_name', 'pub_date']
	search_fields = ['user_name']

class WineAdmin(admin.ModelAdmin):
	model = Wine
	list_display = ('title', 'time', 'wine_type')
	list_filter = ['title']
	search_fields = ['title', 'time']



admin.site.register(Wine, WineAdmin),
admin.site.register(Review, ReviewAdmin),