from urllib.parse import urlparse
from django.urls import path
from .views import AsmaalhusnaList, AsmaalhusnaDetail

urlpatterns = [
    path('', AsmaalhusnaList.as_view()),
    path('<int:pk>/', AsmaalhusnaDetail.as_view()),    
]