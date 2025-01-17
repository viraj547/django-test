from django.urls import path,include
from .web import get_product_listing,web_create_dynamic_product,export_data

urlpatterns = [
    path("",get_product_listing,name="product_listing"),
    path("create-dynamic-product",web_create_dynamic_product,name="create_dynamic_product"),
    path("export-data",export_data,name="export_data"),
]