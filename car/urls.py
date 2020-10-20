from django.urls import path
from .views import CarListView, UsedCarListView,NewCarListView,CarDetailView, CarCreateView,CarUpdateView,CarDeleteView,CarOrderView,AdminView,MyOrderView, OrderDetailView,MyorderDeleteView,OrderUpdateView,ProcessOrderView
from . import views
urlpatterns = [
    path('', CarListView.as_view(), name='car-home'),
    path('about/',views.about,name='car-about'),
    path('used-cars/',UsedCarListView.as_view(),name='car-usedcars'),
    path('new-cars/',NewCarListView.as_view(),name='car-newcars'),
    path('admin-car/',AdminView.as_view(),name='car-admin'),
    path('myorders/',MyOrderView.as_view(),name='car-myorders'),


    path('car/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('myorders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

    path('car/new/', CarCreateView.as_view(), name='car-create'),


    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    path('car/<int:pk>/orderupdate/', OrderUpdateView.as_view(), name='order-update'),

    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
    path('car/<int:pk>/orderdelete/', MyorderDeleteView.as_view(), name='order-delete'),
    path('car/<int:car_id>/order', CarOrderView.as_view(), name='car-order'),
     path('car/<int:pk>/process', ProcessOrderView.as_view(), name='process'),









]
