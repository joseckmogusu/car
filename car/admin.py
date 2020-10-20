from django.contrib import admin
from .models import car_db,order
from users.forms import UserRegisterForm
admin.site.site_header= "Car Administration"

# Register your models here.
admin.site.register(car_db)
admin.site.register(order)
