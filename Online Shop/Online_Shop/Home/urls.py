from django.urls import path
from . import views
app_name='Home'
urlpatterns = [
    path('',views.home,name='homepage'),
    path('<slug:c_slug>/',views.home,name='products_by_category'),
    path('<slug:cat_slug>/<slug:product_slug>/',views.product_detail,name='product_detail'),
    path('search/?',views.search,name="search")
]
