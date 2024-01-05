from django.urls import path
from .views import FishList, FishDetail
from .views import like_unlike_fish

urlpatterns = [
    path('fishes', FishList.as_view()),
    path('fishes/<int:pk>', FishDetail.as_view()),
    path('fishes/<int:pk>/like-unlike/', like_unlike_fish, name='like-unlike-fish'),

]