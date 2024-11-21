from django.urls import path
from .views import MembresiaListView

urlpatterns = [
    path('', MembresiaListView.as_view(), name='memberships_list'),
]
