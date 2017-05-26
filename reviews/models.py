from django.db import models
import numpy as np



class Wine(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=300, null=True)
    image = models.FileField(null=True, blank=True)
    background_image = models.FileField(null=True, blank=True)
    time = models.DateTimeField('date published', null=True)
    wine_type = (
    	('red', 'red'),
    	('green', 'green'),
    	('blue', 'blue'),
    	)
    wine_type = models.CharField(max_length=200, choices=wine_type, null=True)
    # Working hours accoeding to the days
    mon = models.CharField(max_length=200, default=	'Yes')
    tue = models.CharField(max_length=200, default=	'Yes')
    wed = models.CharField(max_length=200, default=	'Yes')
    thu = models.CharField(max_length=200, default=	'Yes')
    fri = models.CharField(max_length=200, default=	'Yes')
    sat = models.CharField(max_length=200, default=	'Yes')
    sun = models.CharField(max_length=200, default=	'Yes')

    # more information about the business
    take_reservations  = models.CharField(max_length=200, default=	'Yes')
    delivery  = models.CharField(max_length=200, default=	'Yes')
    take_out  = models.CharField(max_length=200, default='Yes')
    Accept_credit_card  = models.CharField(max_length=200, default='Yes')
    accept_android_pay  = models.CharField(max_length=200, default='Yes')
    good_for  = models.CharField(max_length=200, default='Yes')
    parking  = models.CharField(max_length=200, default='Yes')
    bike_parking  = models.CharField(max_length=200, default='Yes')
    wheelchair_accessible  = models.CharField(max_length=200,default='Yes')
    good_for_kids  = models.CharField(max_length=200, default='Yes')
    attire  = models.CharField(max_length=200, default='Yes')
    noise_level = models.CharField(max_length=200, default='Yes')
    music  = models.CharField(max_length=200, default='Yes')
    good_for_dancing  = models.CharField(max_length=200, default='Yes')
    alcohol  = models.CharField(max_length=200, default='Yes')
    happy_hour  = models.CharField(max_length=200, default='Yes')
    best_night  = models.CharField(max_length=200, default='Yes')
    coat_check  = models.CharField(max_length=200, default='Yes')
    smoking  = models.CharField(max_length=200, default='Yes')
    outdoor_seating  = models.CharField(max_length=200, default='Yes')
    wifi  = models.CharField(max_length=200, default='Yes')
    has_tv  = models.CharField(max_length=200, default='Yes')
    waiter_service  = models.CharField(max_length=200, default='Yes')
    caters  = models.CharField(max_length=200, default='Yes')
    has_pool_table = models.CharField(max_length=200, default='Yes')
    gender_neutral_rooms  = models.CharField(max_length=200, default='Yes')






    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)
        
    def __unicode__(self):
        return self.title


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    wine = models.ForeignKey(Wine)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=2000)
    rating = models.IntegerField(choices=RATING_CHOICES)