from django.urls import path
from .views import get_info, get_products, detail



urlpatterns = [
    path('', get_info, name='get_info'),
    path('product/<int:pk>', get_products, name='get_product'),
    path('product/detail/<int:pk>', detail, name='detail')
]