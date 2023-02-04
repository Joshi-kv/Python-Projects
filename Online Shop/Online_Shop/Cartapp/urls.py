from django.urls import path
from . import views
app_name='Cartapp'
urlpatterns = [
    path('',views.cart_detail,name='cart_detail'),
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('remove/<int:product_id>/',views.remove_item,name='remove_item'),
    path('delete/<int:product_id>/',views.item_delete,name='item_delete'),
]
