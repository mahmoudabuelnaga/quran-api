from django.urls import path
from .views import CategoryList, CategoryDetail, ComponentList, ComponentDetail, ContainerList, ContainerDetail

urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),

    path('category/container/', ContainerList.as_view()),
    path('category/container/<int:pk>/', ContainerDetail.as_view()),

    path('category/container/component/', ComponentList.as_view()),
    path('category/container/component/<int:pk>/', ComponentDetail.as_view()),

]