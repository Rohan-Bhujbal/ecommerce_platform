from . import views
from django.urls import path

urlpatterns = [
    path('product_add', views.product_add_view, name='product_add'),
    path('product_edit', views.product_edit_view, name='product_edit'),
    path('product_list', views.product_list_view, name='product_list'),
]