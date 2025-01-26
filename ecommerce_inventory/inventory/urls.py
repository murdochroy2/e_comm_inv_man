from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from inventory.api_views import InventoryAPIView, InventoryStockAPIView, CategoryAPIView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # API documentation
    path('api/docs/', include_docs_urls(title='Inventory API')),
    
    # Category endpoints
    path('api/categories/', CategoryAPIView.as_view(), name='category-list'),
    path('api/categories/<int:pk>/', CategoryAPIView.as_view(), name='category-detail'),
    
    # Product CRUD endpoints
    path('api/inventory/', InventoryAPIView.as_view(), name='inventory-list'),
    path('api/inventory/<str:pk>/', InventoryAPIView.as_view(), name='inventory-detail'),
    
    # Stock management endpoints
    # path('api/inventory/<str:pk>/stock/', InventoryStockAPIView.as_view(), name='inventory-stock'),
]

# Add format suffix patterns to support .json and .api formats
urlpatterns = format_suffix_patterns(urlpatterns) 