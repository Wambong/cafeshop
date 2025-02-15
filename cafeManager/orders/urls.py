from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'orders', views.OrderViewSet)
urlpatterns = [
    path('home/', views.home, name='home'),
    path('orders/', views.order_list, name='order_list'),
    path('add_item/', views.add_item, name='add_item'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('', views.add_order, name='add_order'),
    path('delete/<int:order_id>/', views.delete_order, name='delete_order'),
    path('search/', views.search_orders, name='search_orders'),
    path('update/<int:order_id>/', views.update_status, name='update_status'),
    path('revenue/', views.revenue_report, name='revenue_report'),
    path('api/', include(router.urls)),
]