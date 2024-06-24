from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_create_view, name='product-create'),
    path('<int:pk>/update', views.product_update_view, name='product-update'),
    path('<int:pk>/delete', views.product_destroy_view, name='product-destroy'),
    path('<int:pk>/', views.product_detail_view, name='product-detail'),
    path('list/', views.product_list_view, name='product-list'),
]