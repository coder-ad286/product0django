from django.urls import path
from .views import apiOverview,fetchProducts

urlpatterns=[
    path("",apiOverview,name="api-overview"),
    path('fetch-products/',fetchProducts,name="fetch-products")
]