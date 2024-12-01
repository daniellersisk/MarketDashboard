from django.urls import path
from .views import InstrumentListView

urlpatterns = [
    path('stocks/', InstrumentListView.as_view(), name='stock-list'),
]