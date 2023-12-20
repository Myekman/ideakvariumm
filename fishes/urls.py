from django.urls import path
from .views import FishList, FishDetail

urlpatterns = [
    path('fishes', FishList.as_view()),
    path('fishes/<int:pk>', FishDetail.as_view())
]