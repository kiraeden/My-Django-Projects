from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('index/', views.ProductView.as_view(), name='product_index'),
    path('addProduct/', views.AddProductView.as_view(), name='addProduct'),
    path('addNewProduct/', views.addProduct, name='addNewProduct'),
    path('editProduct/<int:pk>/', views.EditProductView.as_view(), name='editProduct'),
    path('processEdit/', views.editProduct, name='edit_product'),
    path('deleteProduct/', views.deleteProduct, name='delete_product'),
]