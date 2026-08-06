from django.urls import path
from .views import (vendor_store_view, 
                    home_view, 
                    register_view,
                    CustomLoginView, 
                    CustomLogoutView, 
                    dashboard_view,
                    add_product_view,
                    delete_product_view    
)

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/product/add', add_product_view, name='add_product'),
    path('dashboard/product/delete/<int:pk>/', delete_product_view, name='delete_product'),
    path('register/', register_view, name='register'),
    path('store/<slug:slug>/', vendor_store_view, name='vendor_store'),
]
