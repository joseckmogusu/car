from django.db import models
from django.utils import timezone
from datetime import datetime, date
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.core.exceptions import ValidationError
from uuid import uuid4
from django.db import IntegrityError
from phonenumber_field.modelfields import PhoneNumberField
from model_utils import Choices


'''choices = (('pending', 'pending'),
             ('processed', 'processed'), 
        ('done', 'done'),
        
        )'''




# Create your models here.
class car_db(models.Model):
	#car_id = models.CharField(primary_key=True, max_length=32, editable=False, unique=True)
	car_id=models.AutoField(primary_key=True, editable=False,unique=True)
	car_make=models.CharField("Make (Toyota,Subaru,...)",max_length=100)
	car_model=models.CharField("Model (Harrier...)",max_length=100)
	car_color=models.CharField(max_length=100)
	car_year=models.DateTimeField("Year (mm/dd/2020)",auto_now_add=False,auto_now=False,blank=True,null=True)
	car_price=models.IntegerField("Price (Ksh)")
	car_loc=models.CharField("Location ",max_length=100)
	car_fuel=models.CharField("Fuel (Petrol,Diesel)",max_length=20)
	CONDITION = Choices('Used','international Used','New')
	condition_type= models.CharField(choices=CONDITION,max_length=20)
	
	car_mileage=models.IntegerField("Mileage") 
	car_transmission=models.CharField("Transmission (Auto, Manual,Semi)",max_length=20)
	date_posted=models.DateTimeField(auto_now=True)
	author=models.ForeignKey(User, on_delete=models.CASCADE)

	#pic uploads  
	image_front=models.ImageField(default='cardef.png',upload_to='front_pics')
	image_side=models.ImageField(default='cardef.png',upload_to='side_pics')
	image_back=models.ImageField(default='cardef.png',upload_to='back_pics')
	image_full=models.ImageField(default='cardef.png',upload_to='full_pics')

	class Meta:
		verbose_name_plural= "Cars"


	def __str__(self):
		return str(self.car_id)


	
		
	def save(self,*args,**kwargs):
		super().save()

		img_front=Image.open(self.image_front.path)
		img_side=Image.open(self.image_side.path)
		img_back=Image.open(self.image_back.path)
		img_full=Image.open(self.image_full.path)



		if img_front.height>300 or img_front.width>300 or img_side.width>300 or img_side.height> 300 or img_back.height>300 or img_back.width>300 or img_full.height>300 or img_full.width>300:
			output_size=(300,300)
			img_front.thumbnail(output_size)
			img_side.thumbnail(output_size)
			img_back.thumbnail(output_size)
			img_full.thumbnail(output_size)

			img_front.save(self.image_front.path)
			img_side.save(self.image_side.path)
			img_back.save(self.image_back.path)
			img_full.save(self.image_full.path)
		#if self.car_id:
			#super(car_db,self).save(*args,**kwargs)
			#return
		#unique=False
		#while not unique:
			#try:
				#self.car_id= uuid4().hex
				#super(car_db, self).save(*args, **kwargs)
			#except IntegrityError:
				#self.car_id= uuid4().hex
			#else:
				#unique = True



	def get_absolute_url(self):
		return reverse('car-detail', kwargs={'pk':self.pk})

def future(value):
	today=date.today()
	if value <today:
	  	raise ValidationError('The date cannot be in the past')

class order(models.Model):
	order_id=models.AutoField(primary_key=True,editable=False, unique=True)
	date_placed=models.DateTimeField(auto_now=True)
	date=models.DateField("Viewing Date (mm/dd/2020)",auto_now_add=False,auto_now=False,null=True, validators=[future])
	
	order_email=models.EmailField("Confirm order Email",null=True)
	order_phone=PhoneNumberField("Confirm order Mobile",null=True)
	STATUS = Choices('pending', 'processed','done')
	status = models.CharField(choices=STATUS, default=STATUS.pending, max_length=20)
	car_db=models.ForeignKey(car_db,on_delete=models.CASCADE,null=True, verbose_name='car')
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, verbose_name='customer')

    
	

	class Meta:
		verbose_name_plural= "Orders"


	#def save(self, *args, **kwargs):
	#	if self.order_id:
	#		super(order, self).save(*args, **kwargs)
	#		return
	#	unique = False
	#	while not unique:
	#		try:
	#			self.order_id= uuid4().hex
	#			super(order, self).save(*args, **kwargs) 
	#		except IntegrityError:
	#			self.order_id = uuid4().hex
	#		else:
	#			unique = True
	

	def __str__(self):
		#return 'order: {} {} {} {}'.format(str(self.order_id), self.date_placed, self.date,self.order_email,self.order_phone)
		return str(self.order_id)



	


	def get_absolute_url(self):

		return reverse('car-myorders')
	
		





