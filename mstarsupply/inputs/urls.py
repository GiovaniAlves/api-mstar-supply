from inputs.views import inputs_manager, inputs_manager_detail_and_change

from django.urls import path

urlpatterns = [
    path('', inputs_manager),
    path('<int:pk>/', inputs_manager_detail_and_change),
]