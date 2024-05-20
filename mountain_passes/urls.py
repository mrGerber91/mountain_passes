from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/submitData', views.PerevalAddedViewSet, basename='submitData')

urlpatterns = [
    path('', include(router.urls)),
    path('getUserData/', views.get_user_data, name='get_user_data'),
]
