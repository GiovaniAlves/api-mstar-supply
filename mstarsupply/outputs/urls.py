from outputs.views import outputs_manager, outputs_manager_detail_and_change, outputs_by_month

from django.urls import path

urlpatterns = [
    path('', outputs_manager),
    path('<int:pk>/', outputs_manager_detail_and_change),
    path('by_month/<int:month>/', outputs_by_month),
]