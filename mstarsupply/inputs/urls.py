from inputs.views import inputs_manager, inputs_manager_detail_and_change, inputs_by_month

from django.urls import path

urlpatterns = [
    path('', inputs_manager),
    path('<int:pk>/', inputs_manager_detail_and_change),
    path('by_month/<int:month>/', inputs_by_month),
]