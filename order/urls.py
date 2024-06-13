from . import views
from django.urls import path

urlpatterns = [
    path('order_list', views.order_list_view, name='order_list'),
    path('order_add', views.order_add_view, name='order_add')
]