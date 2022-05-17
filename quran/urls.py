from django.urls import path
from .views import ReaderList, ReaderDetail #, RecitationsList, RecitationsDetail

urlpatterns = [
    path('', ReaderList.as_view()),
    path('<int:pk>/', ReaderDetail.as_view()),
    # path('recitations/', RecitationsList.as_view()),
    # path('recitations/<int:pk>/', RecitationsDetail.as_view()),
]