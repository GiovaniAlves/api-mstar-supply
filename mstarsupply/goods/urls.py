from goods.views import goods_manager, goods_manager_detail_change_and_delete

from django.urls import path

urlpatterns = [
    path('', goods_manager),
    path('<int:pk>/', goods_manager_detail_change_and_delete),
]