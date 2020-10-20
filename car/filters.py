import django_filters
from django_filters import DateFilter

from .models import car_db,order
from django.contrib.auth.models import User


class CarFilter(django_filters.FilterSet):


	class Meta:
		model=car_db
		fields=['car_make','car_model','car_year','car_color','car_price']

class OrderFilter(django_filters.FilterSet):
	class Meta:
		model=order
		fields=['order_id','date_placed','date']

	