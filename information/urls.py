from django.urls import path
from .views import(
    InfoListAPIView,
    InfoUpdateApiView,
    InfoDestroyApiView,
    InfoCreateAPIView
)

urlpatterns = [

    path('info_list/', InfoListAPIView.as_view(), name='info_list'),
    path('info_create/',InfoCreateAPIView.as_view(), name='info_create'),
    path('info_update/<int:id>/', InfoUpdateApiView.as_view(), name='info_update'),
    path('info_delete/<int:id>/', InfoDestroyApiView.as_view(), name='info_delete'),

]
