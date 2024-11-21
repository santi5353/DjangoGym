from django.urls import path
from .views import ServicioListView

urlpatterns = [
    path('', ServicioListView.as_view(), name='services_list'),
]
