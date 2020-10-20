from django.shortcuts import render,get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView, UpdateView,DeleteView
from django.contrib.auth.models import User
from .models import car_db,order
from .filters import CarFilter,OrderFilter

from django.contrib import messages


#def home(request):
	#context={
	#'cars':car_db.objects.all(),
	#'n_cars':car_db.objects.extra(where=["condition_type='New' or 'new' "]),
	#Entry.objects.extra(where=["foo='a' OR bar = 'a'", "baz = 'a'"])
	#'o_cars':car_db.objects.filter(Q(condition_type="international Used") | Q(condition_type="Used") |Q(condition_type="used"))

	
	#}
	#return render(request,'car/home.html',context)


	
class CarListView(ListView):
	model=car_db
	#cars=car_db.objects.all()
	template_name='car/home.html'
	#context_object_name='cars'
	ordering=['-date_posted']
	paginate_by=4
	def get_context_data(self,**kwargs):

		context = super(CarListView, self).get_context_data(**kwargs)
		context['cars'] = car_db.objects.all()

		context['myfilter'] = CarFilter(self.request.GET, queryset=self.get_queryset())
		return context


 
        

       
class UsedCarListView(ListView):
	model=car_db
	template_name='car/usedcars.html'
	context_object_name='cars'
	paginate_by=8

	def get_queryset(self):
		return car_db.objects.filter(condition_type__icontains='used').order_by('-date_posted')


	


class NewCarListView(ListView):
	model=car_db	
	template_name='car/newcars.html'
	context_object_name='cars'
	paginate_by=8

	def get_queryset(self):
		return car_db.objects.filter(condition_type__iexact='New').order_by('-date_posted')

	



#DetailView

class CarDetailView(DetailView):
	model=car_db
	template_name='car/car_detail.html'
	

class CarCreateView(LoginRequiredMixin,CreateView):
	model= car_db
	template_name='car/car_form.html'
	fields= ['car_make','car_model','car_color', 'car_year', 'car_price','car_loc', 'car_fuel', 'condition_type','car_mileage','car_transmission', 'image_full','image_side','image_front','image_back']
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

 
class CarUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model= car_db
	template_name='car/car_form.html'
	fields= ['car_make','car_model','car_color', 'car_year', 'car_price','car_loc', 'car_fuel', 'condition_type','car_mileage','car_transmission', 'image_full','image_side','image_front','image_back']
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)
	def test_func(self):
		car=self.get_object()
		if self.request.user==car.author:
			return True
		return False








class CarDeleteView(LoginRequiredMixin,UserPassesTestMixin ,DeleteView):
	model=car_db
	template_name='car/post_confirm_delete.html'
	success_url='/'
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)
	def test_func(self):
		car=self.get_object()
		if self.request.user==car.author:
			return True
		return False

class MyorderDeleteView(LoginRequiredMixin,UserPassesTestMixin ,DeleteView):
	model=order
	template_name='car/order_confirm_delete.html'
	success_url='/'
	def form_valid(self,form):
		form.instance.user=self.request.user
		return super().form_valid(form)
	def test_func(self):
		order=self.get_object()
		if self.request.user==order.user:
			return True
		return False




class CarOrderView(LoginRequiredMixin,CreateView):
	model=order
	template_name='car/car_order.html'
	fields=['date','order_email','order_phone']
	def form_valid(self,form):
		form.instance.user=self.request.user
		car_id=self.kwargs.get("car_id")
		form.instance.car_db_id= car_id
		#form.instance.car_db=self.kwargs.get("car_id")
		#car_db.objects.filter(car_id=self.kwargs.get("car_id"))
		
		#return super(CarCreateView,self).form_valid(form)

		return super().form_valid(form)




class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
	def test_func(self):
		return self.request.user.is_superuser or self.request.user.is_staff

class AdminView(AdminStaffRequiredMixin,ListView): 


	model = order
	template_name = 'car/admin.html'
	context_object_name='orders'
	#fields = ['first_name', 'username', 'is_active']
	


	#def get_queryset(self):
		#orderalls=order.objects.all().values_list('pk',flat=True)
		
		

		#for orderall in range(len(orderalls)):
			#car_item= order.objects.filter(car=1)
			#cars= car_db.objects.all().values_list('pk', flat=True)
			
			

			#for car in cars:
				#orders=order.objects.all()
				#car=car_db.objects.get(car_id=car)
				#orders=car.order_set.all()
			#orders=order.objects.all()
			#car=car_item
			#return order.objects.all().values_list('car_db','car_db__image_front', 'car_db__car_model')
			#Points.objects.filter(user_id=id).values_list('user_id', 'lat', 'lon', 'user_id__username')
		#return orders
	def get_context_data(self,**kwargs):

		context = super(AdminView, self).get_context_data(**kwargs)
		orderalls=order.objects.all().values_list('pk',flat=True)
		for orderall in  range(len(orderalls)):
			cars=car_db.objects.all().values_list('pk',flat=True)
			for car in cars:
				orders=order.objects.all()
				
		context['orders'] = orders
		context['myfilter'] = OrderFilter(self.request.GET, queryset=self.get_queryset())
		context['pending'] = orders.filter(status='pending')
		context['processed'] = orders.filter(status='processed')
		context['processed'] = orders.filter(status='processed')


		return context





		
		
		
		return context


		
		#queryset = sorted(chain(order,car_item,orders))

class MyOrderView(LoginRequiredMixin,ListView):
	model=order
	template_name='car/myorders.html'
	context_object_name='myorders'
	def form_valid(self,form):
		form.instance.user=self.request.user
		return super().form_valid(form)
	def test_func(self):
		car=self.get_object
		if self.request.user==order.user:
			return True
		return False

	def get_queryset(self):

		
		myorders=order.objects.filter(user=self.request.user).order_by('-date_placed')
		return myorders
		
class OrderDetailView(DetailView):
	model=order
	template_name='car/order_detail.html'

class OrderUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model= order
	template_name='car/order_form.html'
	fields= ['order_email','order_phone', 'date', 'car_db']
	def form_valid(self,form):
		form.instance.user=self.request.user
		return super().form_valid(form)
	def test_func(self):
		order=self.get_object()
		if self.request.user==order.user:
			return True
		return False




	


class ProcessOrderView(AdminStaffRequiredMixin,UpdateView):
	model=order 
	template_name='car/process.html'
	context_object_name='orders'
	fields=['status','order_email']
	
def about(request):
	return render(request,'car/about.html')

def usedcars(request):
	return render(request,'car/usedcars.html')
def newcars(request): 
	return render(request,'car/newcars.html')

