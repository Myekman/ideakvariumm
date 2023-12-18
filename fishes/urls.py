from django.urls import path
from .views import FishList

urlpatterns = [
    path('', FishList.as_view()),
    # path('fishes/<int:pk>/', views.FishostDetail.as_view())
]