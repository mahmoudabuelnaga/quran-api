from django.urls import path
from .views import BroadcastingListAPIView, BroadcastingRetrieveAPIView

urlpatterns = [
    path('', BroadcastingListAPIView.as_view()),
    path('<int:pk>/', BroadcastingRetrieveAPIView.as_view()),
]